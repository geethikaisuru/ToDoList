import zipfile
import pathlib

def make_zip(filepaths, folder):
    dest_path = pathlib.Path(folder,"archive.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname = filepath.name)

if __name__ == "__main__":
    make_zip(filepaths = ["main.py", "main.py"], folder = "dest")