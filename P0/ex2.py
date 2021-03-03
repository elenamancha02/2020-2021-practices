import Seq0
FOLDER = "./sequences/"
ID = "ADA.txt"
#we are creating this path ./sequences/ADA.txt

U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)
print ("The first 20 bases are:", U5_Seq[0:20])
