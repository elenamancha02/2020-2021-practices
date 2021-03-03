from pathlib import Path


FILENAME = "U5.txt"
file_contents = Path(FILENAME).open()
next(f)
print(file_contents)