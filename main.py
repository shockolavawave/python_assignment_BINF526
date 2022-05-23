from Bio import Seq, SeqIO


def main():
    # getting the file
    in_file = list(SeqIO.parse("files/sequence.fasta", "fasta"))

    # extracting sequence
    seq1 = in_file[0].seq
    print(seq1)


main()
