def main():
    matrix_str = "4 2\n5 3"
    filename = "matrix.txt"
    print(f"write matrix {matrix_str} to \'{filename}\'")
    write_matrix(matrix_str, filename)
    matrix = read_matrix(filename)
    print("read matrix:", matrix)
    print("determinant =", matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1])


def write_matrix(strmat, filename):
    with open(filename, "w") as f:
        f.write(strmat)


def read_matrix(filename):
    matrix = []
    with open(filename, "r") as f:
        lines = f.readlines()
        lines = [line.rstrip("\n") for line in lines]
        lines = [line.split(" ") for line in lines]
        for line in lines:
            row = [int(num) for num in line]
            matrix.append(row)
    return matrix


if __name__ == "__main__":
    main()
