#!/usr/bin/env python3
"""Getting the determinant of a matrix"""


def determinant(matrix):
    """Function that calculates the determinant of a matrix """
    if not all(type(row) == list for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or type(matrix) != list:
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
<<<<<<< HEAD
    if not all(len(r) == len(matrix) for r in matrix):
=======
    if not all(len(e) == len(matrix) for e in matrix):
>>>>>>> 7d6e11351dd75159088b0a0af41e10c18be776fe
        raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
<<<<<<< HEAD
        x = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return x
    det = 0
    for x, num in enumerate(matrix):
        temp = []
        P = matrix[0][x]
        for row in matrix[1:]:
            new = []
            for j in range(len(matrix)):
                if j != x:
                    new.append(row[j])
            temp.append(new)
        det += P * determinant(temp) * (-1) ** x
=======
        c = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return c
    det = 0
    for c, num in enumerate(matrix):
        temp = []
        P = matrix[0][c]
        for row in matrix[1:]:
            new = []
            for d in range(len(matrix)):
                if d != c:
                    new.append(row[d])
            temp.append(new)
        det += P * determinant(temp) * (-1) ** c
>>>>>>> 7d6e11351dd75159088b0a0af41e10c18be776fe
    return det
