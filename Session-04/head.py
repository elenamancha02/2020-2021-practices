#First line of the RNU6_269P.txt file:
#>16 dna:chromosome chromosome:GRCh38:16:58377452:58378748:-1

from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
if file_contents[0]== '>':
    print(file_contents)
else:
    print('Sorry, your file cant be printed')