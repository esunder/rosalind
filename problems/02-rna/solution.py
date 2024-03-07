import sys


coding = {'A':'A', 'C':'C', 'G':'G', 'T':'U'}
def main():
    with open(sys.argv[1]) as infile:
        lines = infile.readlines()
        sequence = lines[0].strip()
        rna = ''
        for i in sequence:
            rna += coding[i]
        print(rna)

if __name__ == "__main__":
    main()