import argparse
from pathlib import Path
import re
import os
from argparse import ArgumentParser

# working-directory
WORK_DIR = Path().resolve()
EXEC_DIR = Path(__file__).parent

SEARCH_DIRECTORIES = WORK_DIR / Path("directories.txt")
EXCLUDES = WORK_DIR / Path("exclude.txt")

VERSION = "v0.1"

def main():
	# parse the external files for search directories and excludes
	re_dir_split = re.compile("\r?\n")
	excludes_extern = re_dir_split.split(EXCLUDES.read_text()) if EXCLUDES.exists() else []
	directories_extern = re_dir_split.split(SEARCH_DIRECTORIES.read_text()) if SEARCH_DIRECTORIES.exists() else ["."]

	# setup CLI-arguments
	parser = ArgumentParser(prog="find_duplicates")
	parser.add_argument("-o", "--output", help="the file to write the duplicates to (default: duplciates.txt)", action="store", default="duplicates.txt")
	parser.add_argument("-x", "--exclude", help="directories to be excluded", action="extend", nargs="*", default=excludes_extern)
	parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
	parser.add_argument("DIR", action="extend", help="the directories to be searched for duplicates", nargs="*", default=directories_extern)
	args = parser.parse_args()

	# pad the search-dirs with parentheses
	search_dirs = [f"\"{WORK_DIR / dir}\"" for dir in args.DIR]

	jdupes_excludes = [f"-X nostr:\"{convert_exclude(exclude)}\"" for exclude in args.exclude]

	# construct the jdupes-command
	jdupes_command = " ".join([
		f"{EXEC_DIR}/jdupes.exe",
		"-rO", # recursive and sort by order of SEARCH_DIRS
		*jdupes_excludes,
		*search_dirs])
	
	print (jdupes_command)

	# run jdupes and capture its output
	jdupes_stream = os.popen(jdupes_command)
	jdupes_output = jdupes_stream.read()

	# write the found duplicates into a file
	Path(args.output).write_text(jdupes_output)

def convert_exclude(_exclude):
	match os.name:
		case "nt":
			exclude = _exclude.replace("/", "\\")
			exclude = re.sub(r"\\+", r"\\\\", exclude)
		case "posix":
			exclude = _exclude.replace("\\", "/")
		case _:
			...
	
	return exclude

def print_license():
	license_text = []

	# create paths for license-files
	for lic in LICENSE_FILES:
		license_text.append((EXEC_DIR / lic).read_text())

	license_text = " \nLICENSE\n \n" + "\n \n \n".join(license_text)

	return license_text

if __name__ == "__main__":
	main()