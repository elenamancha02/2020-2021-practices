
import termcolor
class Seq:
    def __init__(self, strbases="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == "NULL":
            print("NULL seq created")
            self.strbases = strbases
        else:
            if self.is_valid_sequence_2(strbases):
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = "ERROR"
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
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)
def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq
