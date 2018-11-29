import sys

def read_file(file):
    with open(file) as inputfile:
        lines = [line.split() for line in inputfile]
        return lines, len(lines)

def main():
    if(len(sys.argv) < 2):
        print("Please include an input file and try again.")
        sys.exit(1)
    filename = sys.argv[1]