from genericpath import isdir
from pathlib import Path
import re
from argparse import ArgumentParser

WORK_DIR = Path().resolve()
EXEC_DIR = Path(__file__).parent

SEARCH_DIRECTORIES = WORK_DIR / Path("directories.txt")
EXCLUDES = WORK_DIR / Path("exclude.txt")

VERSION = "v0.1"

re_dir_split = re.compile("\r?\n")
excludes_extern = re_dir_split.split(EXCLUDES.read_text()) if EXCLUDES.exists() else []
directories_extern = re_dir_split.split(SEARCH_DIRECTORIES.read_text()) if SEARCH_DIRECTORIES.exists() else ["."]

def main():
	parser = ArgumentParser(prog="search_empty")
	parser.add_argument("-o", "--output", action="store", default="empty.txt")
	parser.add_argument("-x", "--exclude", action="extend", nargs="*", default=excludes_extern)
	parser.add_argument("-d", "--delete", action="store_true")
	parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
	parser.add_argument("DIR", action="extend", nargs="*", default=directories_extern)
	args = parser.parse_args()

	exclude_dirs = [WORK_DIR / d for d in args.exclude]
	search_dirs = [WORK_DIR / d for d in args.DIR]

	empty_dir_list = []

	for search_dir in search_dirs:
		for p in Path(search_dir).rglob("*"):
			exclude = False
			for exclude_dir in exclude_dirs:
				if exclude_dir in p.parents:
					exclude = True
					break

			if not exclude and p.is_dir() and not any(p.iterdir()): # is directory and has no children
				empty_dir_list.append(p)

	# remove duplicates
	empty_dir_list = list(set(empty_dir_list))

	if (args.delete):
		for empty_dir in empty_dir_list:
			empty_dir.rmdir()
	else:
		Path(args.output).write_text("\n".join([str(d) for d in empty_dir_list]))

if __name__ == "__main__":
	main()