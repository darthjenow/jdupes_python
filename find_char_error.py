from pathlib import Path
from typing import List
import tempfile

WORK_DIR = Path().resolve()
ERROR_FILE = WORK_DIR / "error_files.txt"

TEMP_FILE = tempfile.NamedTemporaryFile("w", encoding="charmap")
TEMP_FILE.close()
TEMP_FILE_PATH = Path(TEMP_FILE.name)

def main():
	# go through every file
	error_files = enter_dir(WORK_DIR)

	ERROR_FILE.write_text("\n".join(error_files), encoding="utf-8")

def enter_dir(dir: Path) -> List:
	error_files = []

	for f in dir.iterdir():
		if f.is_dir():
			new_error_files = enter_dir(f)

			if len(new_error_files) > 0:
				error_files.append(*new_error_files)
		
		try:
			TEMP_FILE_PATH.write_text(str(f))
		except (UnicodeDecodeError, UnicodeEncodeError):
			error_files.append(str(f))

	return error_files


if __name__ == "__main__":
	main()