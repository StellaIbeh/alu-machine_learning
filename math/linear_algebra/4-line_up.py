#!/usr/bin/env python3
''' Adds two arrays element-wise'''


def add_arrays(arr1, arr2):
    ''' This function adds two arrays element-wise'''
    if len(arr1) == len(arr2):
        return [arr1[a] + arr2[a] for a in range(len(arr1))]
    else:
        return None
