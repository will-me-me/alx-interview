#!/usr/bin/python3
"""Roatate 2D Matrix Module."""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix by 90 degrees"""

    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            b, t = r, l

            top_l = matrix[t][l + i]
            matrix[t][l + i] = matrix[b - i][l]
            matrix[b - i][l] = matrix[b][r - i]
            matrix[b][r - i] = matrix[t + i][r]
            matrix[t + i][r] = top_l
        r -= 1
        l += 1
