'''
Transpose of a Matrix의 Docstring
problem link: https://www.deep-ml.com/problems/2
'''

import numpy as np

def transpose_matrix(matrix: list[list[int|float]]) -> list[list[int|float]]:
    result = np.array(matrix).T
    return result