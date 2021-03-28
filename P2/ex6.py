from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 10000
c = Client(IP, PORT)

s = Seq()
s.seq_read_fasta('../Session-04/FRAT1.txt')
count = 0
#for i in range(0, len(s.strbases), 10):
 #  fragment = s.strbases[i:i+10]
 #  count = count + 1
 #  if count == 5:
  #     break
i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    print ("Fragment", count, ":", fragment)
    print(c.talk(fragment))