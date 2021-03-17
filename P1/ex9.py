from seq import Seq


print("-----| Exercise 9 |------")
s = Seq()

s.read_fasta("U5.txt")

print(f"Sequence: (Length: {s.len()}) {s}")
print(f"\tBases: {s.count()}")
print(f"\tRev: {s.reverse()}")
print(f"\tComp: {s.complement()}")