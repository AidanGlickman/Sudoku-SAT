def read_file(file):
    with open(file) as input:
        lines = [line.split() for line in input]
        return lines, len(lines)

def gen_vars(board):
    varlist = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            for i in range(1, len(board) + 1):
                if board[y][x] == str(i):
                    varlist.append(f"{x+1}{y+1}{board[y][x]}")
    return varlist

def gen_known(varlist):
    known = []
    for i in varlist:
        known.append(f"{i} 0")
    return known

def gen_each_filled(varlist, size): # gen_each_filled generates statements for making sure each square is filled
    each_filled = []
    for y in range(1, size):
        for x in range(1, size):
            eachnum = ""
            for k in range(1, size):
                if f"{x}{y}{k}" in varlist:
                    eachnum = ""
                    break
                eachnum += f"{x}{y}{k} "
            if eachnum != "":
                eachnum += "0"
                each_filled.append(eachnum)
    return each_filled

def gen_one_per_row(varlist, size):
    one_per_row = []
    for y in range(1, size):
        for x in range(1, size):
            for k in range(1, size):
                for x_s in range(x+1, size):
                    one_per_row.append(f"-{x}{y}{k} -{x_s}{y}{k} 0")
    return one_per_row

def gen_one_per_col(varlist, size):
    one_per_col = []
    for y in range(1, size):
        for x in range(1, size):
            for k in range(1, size):
                for y_s in range(y+1, size):
                    one_per_col.append(f"-{x}{y}{k} -{x}{y_s}{k} 0")
    return one_per_col

def gen_one_per_block(varlist, size):
    one_per_block = []
    for k in range(1, size):
        for m in range(3):
            for n in range(3):
                for y in range(1, 4):
                    for x in range(1, 4):
                        for y_s in range(y+1, 4):
                            one_per_block.append(f"-{3*m+1}{3*n+y}{k} -{3*m+x}{3*n+y_s}{k} 0")

    for k in range(1, size):
        for m in range(3):
            for n in range(3):
                for y in range(1, 4):
                    for x in range(1, 4):
                        for y_s in range(y, 4):
                            for x_s in range(x+1, 4):
                                one_per_block.append(f"-{3*m+1}{3*n+y}{k} -{3*m+x_s}{3*n+y_s}{k} 0")

    return one_per_block

def gen_clauses(varlist, size):
    clauses = []
    clauses += gen_known(varlist)
    clauses += gen_each_filled(varlist, size)
    clauses += gen_one_per_row(varlist, size)
    clauses += gen_one_per_col(varlist, size)
    clauses += gen_one_per_block(varlist, size)

    return clauses

def combine_clauses(clauses, size):
    clauses_str = "\n".join(clauses)
    return f"p cnf {size**3-1} {len(clauses)}\n{clauses_str}"

def write_solution(solution, filename):
    with open(filename+".out", "w") as out:
        out.write(solution)

def main():
    filename = "sudokus/s01a.txt"
    board, size = read_file(filename)
    varlist = set(gen_vars(board))
    clauses = gen_clauses(varlist, size)
    solution = combine_clauses(clauses, size)
    write_solution(solution, filename)

main()