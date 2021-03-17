import termcolor
class Seq:
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"


    def __init__(self, strbases= NULL_SEQUENCE):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL seq created")
            self.strbases = strbases
        else:
            if self.is_valid_sequence_2(strbases):
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT Sequence detected")
    @staticmethod
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True
    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    @staticmethod
    def print_seqs(seq_list):
        result = ""
        for i in range(len(seq_list)):
            text = "Sequence " + str(i) + ": (Length: " + str(seq_list[i].len()) + "), " + f"{seq_list[i]}"
            termcolor.cprint(text, "cyan")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases
    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self.strbases):
        a, c, g, t = 0, 0, 0, 0
        for ch in dna:
            if ch == "A":
                a += 1
            elif ch == "C":
                c += 1
            elif ch == "G":
                g += 1
            else:
                t += 1
        return a, c, g, t

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq


    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not self.strbases == Seq.NULL_SEQUENCE and not self.strbases == Seq.INVALID_SEQUENCE:
            for ch in dna:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
        return a, c, g, t

    def count(self):
        a, c, g, t = self.count_



