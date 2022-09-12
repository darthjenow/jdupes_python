from multiprocessing.reduction import duplicate
from pathlib import Path
from argparse import ArgumentParser
import re

# working-directory
WORK_DIR = Path().resolve()
EXEC_DIR = Path(__file__).parent

def main():
	# setup CLI-arguments
	parser = ArgumentParser()
	parser.add_argument("-i", "--input", action="store", default="duplicates.txt")
	parser.add_argument("-o", "--output", action="store", default="duplicates")
	args = parser.parse_args()

	file_list = Path(args.input).read_text()

	move_files = create_move_file_list("\n" + file_list)

	if move_files[0] != "":
		for _file in move_files:
			file = Path(_file).relative_to(WORK_DIR)
			new_file = WORK_DIR / args.output / file

			# create the directory
			new_file.parent.mkdir(parents=True, exist_ok=True)

			file.rename(new_file)

def create_move_file_list(jdupes_file_list):
	re_remove = re.compile(r"^$\n^.+$\n", re.MULTILINE)
	re_matches = re_remove.sub("", jdupes_file_list)

	re_matches = re_matches[:-1]

	return re_matches.split("\n")

if __name__ == "__main__":
	main()