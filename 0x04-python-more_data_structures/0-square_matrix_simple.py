#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = []

    for row in matrix:
        rows = []

        for element in row:
            sqr = element**2
            rows.append(sqr)
        matrix_new.append(rows)
    return matrix_new
