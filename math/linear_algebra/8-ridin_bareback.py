#!/usr/bin/env python3
"""Function performs matrix multiplcation"""


def mat_mul(mat1, mat2):
    """Function performs index multiplication"""
    if len(mat1[0]) != len(mat2):
        return None
    matrix = []
    for e in range(len(mat1)):
        matrix.append([])
        for b in range(len(mat2[0])):
            dot = 0
            for c in range(len(mat1[0])):
                dot += mat1[e][c] * mat2[c][b]
            matrix[e].append(dot)
    return matrix

# mat1 = [[1, 2],
#         [3, 4],
#         [5, 6]]
# mat2 = [[1, 2, 3, 4],
#         [5, 6, 7, 8]]
# print(mat_mul(mat1, mat2)
