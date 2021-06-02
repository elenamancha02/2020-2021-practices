import termcolor
from pathlib import Path


class Seq:
    BASES_VALID = ["A", "T", "C", "G"]
    BASES_COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}

    def __init__(self, bases="NULL"):
        if bases == "NULL":
            print("NULL sequence created!")
            self.bases = bases
            return
        for base in bases:
            if base not in Seq.BASES_VALID:
                print("INVALID sequence created!")
                self.bases = "ERROR"
                return
        self.bases = bases
        print("New sequence created!")


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
        file_content = Path(filename).read_text()
        file_content_without_breaklines = file_content.splitlines()
        self.bases = ""
        for line in file_content_without_breaklines[1:]:
            self.bases += line

    def info(self):
        result = f"Sequence: {self}\n"
        result += f"Total length: {self.len()}\n"
        bases_count = self.count()
        for base, count in bases_count.items():
            if count == 0:
                result += f"{base}: {count} (0%)\n"
            else:
                result += f"{base}: {count} ({'{:.1f}'.format((count * 100) / self.len())}%)\n"
        return result

    def most_frequent_base(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return None

        bases_freq = self.count()
        base_result = None
        freq_result = 0
        for base, freq in bases_freq.items():
            if freq > freq_result:
                base_result = base
                freq_result = freq
        return base_result



