from pathlib import Path


class Seq:
    BASES_VALID = ["A", "T", "C", "G"]
    BASES_COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}

    def __init__(self, bases="NULL"):
        if bases == "NULL":
            print("NULL sequence created!")
        else:
            for base in bases:
                if base not in Seq.BASES_VALID:
                    print("INVALID sequence created!")
                    self.bases = "ERROR"
                    return

            print("New sequence created!")

        self.bases = bases

    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)  # count método del tipo 'str'

    def count(self):
        bases_dict = {}
        for base in Seq.BASES_VALID:
            bases_dict[base] = self.count_base(base)
        return bases_dict

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        return self.bases[::-1]

    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        result = ""
        for base in self.bases:  # "ACTGA" | 1º base -> "A"
            result += Seq.BASES_COMPLEMENTS[base]
        return result

    def read_fasta(self, filename):
        file_content = Path(filename).read_text()  # Todo el contenido del fichero (str)
        file_content_without_breaklines = file_content.splitlines()  # Lista con las líneas del fichero
        self.bases = ""
        for line in file_content_without_breaklines[1:]:
            self.bases += line


class Gene(Seq):
    def __init__(self, bases, name=""):
        super().__init__(bases)
        self.name = name
        print("New gene created!")


#s = Seq("AGTACACTGGT")
#print(s)
#print(f"Length: {s.len()}")

#g = Gene("CGTAAC", "Pepito")
#print(g)
#print(f"Length: {g.len()}")
