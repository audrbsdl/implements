'''
Scalar Multiplication of a Matrix
problem link: https://www.deep-ml.com/problems/5
'''
import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	
    matrix = np.array(matrix)
    result = scalar * matrix

    return result