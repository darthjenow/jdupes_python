import os
from pathlib import Path
from zipfile import ZipFile
import importlib

BUILD_DIR = Path("dist")
LICENSE_DIR = Path("license_for_build")
ZIP_DIR = Path("dist/zip")

def main(platform: str):
	print ("creating zip-packages")

	packages = {}

	match platform:
		case "nt":
			suffix = ".exe"
			dist = "windows"
		case "posix":
			suffix = ""
			dist = "linux"
		case _:
			suffix = ""
			dist = "ERROR"

	for license_file in LICENSE_DIR.iterdir():
		build_file = license_file.with_suffix(suffix)

		build_file = BUILD_DIR / build_file.name

		if build_file.exists():
			packages[license_file.stem] = [build_file, license_file]

	# create the zip directory
	ZIP_DIR.mkdir(exist_ok=True)

	for name, packages in packages.items():
		version = importlib.import_module(name).VERSION

		zip_file = ZIP_DIR / f"{name}_{version}_{dist}.zip"
		with ZipFile(zip_file, mode="w") as zip_pack:
			for package in packages:
				zip_pack.write(package, arcname=package.name)

		print (f"{zip_file} has been created")

if __name__ == "__main__":
	main(os.name)