from pathlib import Path
import re
import os
from argparse import ArgumentParser

# working-directory
WORK_DIR = Path().resolve()
EXEC_DIR = Path(__file__).parent

VERSION = "v0.2_DEVEL"

def main():
	# setup CLI-arguments
	parser = ArgumentParser(prog="find_duplicates")
	parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")

	parser.add_argument("-o", "--output", help="the file to write the duplicates to (default: duplciates.txt)", action="store", default="duplicates.txt")
	parser.add_argument("-x", "--exclude", help="directories to be excluded", action="extend", nargs="*")
	parser.add_argument("DIR", action="extend", help="the directories to be searched for duplicates", nargs="*")

	parser.add_argument("-S", "--search-list", help=f"text file with a list of directories to search through", nargs="?")
	parser.add_argument("-X", "--exclude-list", help=f"text file with a list of directories to search through", nargs="?")

	args = parser.parse_args()

	# append the dirs from the files to the list
	re_dir_split = re.compile("\r?\n")
	search_extern = load_file_args(args.search_list)
	exclude_extern = load_file_args(args.exclude_list)

	# pad the search-dirs with parentheses
	search_dirs = [f"\"{convert_path(dir)}\"" for dir in args.DIR]

	if not args.exclude:
		args.exclude = []

	jdupes_excludes = [f"-X nostr:\"{convert_path(exclude)}\"" for exclude in [*args.exclude, *exclude_extern]]

	match os.name:
		case "nt":
			jdupes_path = "jdupes.exe"
		case "posix":
			jdupes_path = "jdupes"
		case "_":
			jdupes_path = "jdupes"

	jdupes_path = str(EXEC_DIR / jdupes_path)

	# construct the jdupes-command
	jdupes_command = " ".join([
		jdupes_path,
		"-rO", # recursive and sort by order of SEARCH_DIRS
		*jdupes_excludes,
		*search_dirs])
	
	# run jdupes and capture its output
	jdupes_stream = os.popen(jdupes_command)
	jdupes_output = jdupes_stream.read()

	# write the found duplicates into a file
	Path(args.output).write_text(jdupes_output, encoding="utf-8")

def load_file_args(f_path: str) -> list[str]:
	entries = []
	if f_path:
		f = Path(f_path)
		content = f.read_text(encoding="utf-8")
		entries = re.split(r"\r?\n", content)

		# remove all empty entries
		entries = [e for e in entries if len(e) > 0]

	return entries


def convert_path(_exclude):
	match os.name:
		case "nt":
			exclude = _exclude.replace("/", "\\")
			exclude = re.sub(r"\\+", r"\\\\", exclude)
		case "posix":
			exclude = _exclude.replace("\\", "/")
		case _:
			...
	
	return exclude

if __name__ == "__main__":
	main()