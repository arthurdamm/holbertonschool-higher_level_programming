#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for submatrix in matrix:
        for i in range(len(submatrix)):
            print("{:d}".format(submatrix[i]),
                  end="\n" if i is len(submatrix) - 1 else " ")
