import Seq0

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if Seq0.is_valid_sequence(strbases):
            print("New sequence created")
            self.strbases = strbases

        else:
            self.strbases = "Error"
            print("incorrect sequence detected!")

    @staticmethod
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True


    def is_valid_sequence(self):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    def __str__(self):
        return self.strbases

    def __len__(self):
        return len(str.bases)


    @staticmethod
    def static_function:
        pass

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")