from Bio import Seq, SeqIO


def print_seq(in_file):

    no_seq = len(in_file)
    print("there are", no_seq, "sequence(s) in the file\n\n")

    tb_printed = ""

    # primary loop for extracting all possible fasta sequences
    for ea in in_file:

        # following are operations made on each
        print(ea.id, "          len:", no_seq)
        print(ea.seq, "\n")


    return tb_printed


def main():
    try:
        # getting the file
        in_file = list(SeqIO.parse("files/sequence.fasta", "fasta"))

        print_seq(in_file)

        #var = in_file[0].seq

    except Exception as e:
        print("something went wrong:", e)


# calling main
main()
