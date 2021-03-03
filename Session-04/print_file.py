from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
print(file_contents)



