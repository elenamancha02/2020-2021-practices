class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
    def  __str__(self):
        return self.strbases
    def __len__(self):
        return len(self.strbases)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for s in range(0, len(seq_list)):
    print(f"Sequence {s} (Length: {seq_list[s].len()}): {seq_list[s]}")
