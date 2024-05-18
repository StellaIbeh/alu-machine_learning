#!/usr/bin/env python3
'''
     def add_matrices2D(mat1, mat2):
    adds two matrices element-wise
'''


def add_matrices2D(mat1, mat2):
    '''
         def add_matrices2D(mat1, mat2):
        adds two matrices element-wise
    '''
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        return [
            [
                mat1[a][b] + mat2[a][b]
                for b in range(len(mat1[0]))
            ]
            for a in range(len(mat1))
        ]
    else:
        return None
