'''
Calculate 2x2 Matrix Inverse
problem link: https://www.deep-ml.com/problems/8
'''
import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    try:
        matrix = np.array(matrix)
        inverse = np.linalg.inv(matrix)
        return inverse
    except np.linalg.LinAlgError:
        return None
