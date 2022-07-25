#!/usr/bin/python3

# N queens puzzle
# Author: Sangwani P. Zyambo
""""
    This program solves the N queens problem
"""


import sys

size = len(sys.argv)
N = sys.argv[1]

def nqueens(size, N)
    if size != 2:
        print("Usage: nqueens N")
        exit(1)
    if not isinstance(N, int):
        ("N must be a number")
        exit(1)
    if N < 4:
        ("N must be at least 4")
        exit(1)
    else:
        return [
                y + x
                for y in nqueens(1, N)
                for x in nqueens(N + 1, N
            ]


