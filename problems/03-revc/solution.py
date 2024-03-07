import sys


complements = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
def main():
    with open(sys.argv[1]) as infile:
        lines = infile.readlines()
        sequence = lines[0].strip()
        revc = ''
        for i in sequence[::-1]:
            revc += complements[i]
        print(revc)

if __name__ == "__main__":
    main()