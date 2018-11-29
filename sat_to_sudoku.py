import sys

def read_file(file):
    with open(file) as inputfile:
        lines = [line.split() for line in inputfile]
        return lines

def sanitize(words):
    saniwords = words[1][99:-1]
    return [x for x in saniwords if not x.startswith('-')]

def solution_to_arr(solution):
    board = [[0] * 9 for i in range(9)]
    for i in solution:
        board[int(i[1])-1][int(i[0])-1] = i[2]
    return board

def arr_to_string(arr):
    result = ""
    for i in arr:
        for j in i:
            result += j + " "
        result = result[:-1] + "\n"
    return result

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            result += j + " "
        result = result[:-1] + "\n"
    return result

def write_to_file(solution, filename):
    with open(filename, "w") as out:
        out.write(solution)

def main():
    if(len(sys.argv) < 2):
        print(f"{sys.argv[0]}: Please include an input file and try again.")
        sys.exit(1)
    filename = sys.argv[1]
    solution = read_file(filename)
    sanitized = sanitize(solution)
    board = solution_to_arr(sanitized)
    soln_string = arr_to_string(board)

    if(len(sys.argv) > 2):
        write_to_file(soln_string, sys.argv[2])
    else:
        print(soln_string)

main()