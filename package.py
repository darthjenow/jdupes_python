from pathlib import Path
from zipfile import ZipFile

BUILD_DIR = Path("dist")
LICENSE_DIR = Path("license_for_build")
ZIP_DIR = Path("dist/zip")

def main():
	print ("creating zip-packages")

	packages = {}

	for build in BUILD_DIR.iterdir():
		if build.suffix in [".exe", ".appimage"]:
			license_file = LICENSE_DIR / build.stem / "LICENSE.txt"

			packages[build.stem] = [build, license_file]

	# create the zip directory
	ZIP_DIR.mkdir(exist_ok=True)

	for name, packages in packages.items():
		zip_file = (ZIP_DIR / name).with_suffix(".zip")
		with ZipFile(zip_file, mode="w") as zip_pack:
			for package in packages:
				zip_pack.write(package, arcname=package.name)

		print (f"{zip_file} has been created")

if __name__ == "__main__":
	main()