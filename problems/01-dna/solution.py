import sys

def main():
    with open(sys.argv[1]) as infile:
        lines = infile.readlines()
        sequence = lines[0].strip()
        dna = {'A':0, 'C':0, 'G':0, 'T':0}
        for i in sequence:
            print(i)
            dna[i] += 1
        print(dna)

if __name__ == "__main__":
    main()