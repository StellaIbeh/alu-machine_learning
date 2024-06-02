#!/usr/bin/env python3
"""Sigma"""


def summation_i_squared(n):
    """Summation"""
    '''
    calculates the summation
    of all numbers from 1 to n
    '''
    # Check if n is a valid number (integer)
    if type(n) is not int or n < 1:
        return None
    sigma_sum = (n * (n + 1) * ((2 * n) + 1)) / 6
    return int(sigma_sum)
