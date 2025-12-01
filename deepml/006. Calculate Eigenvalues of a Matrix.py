'''
Calculate Eigenvalues of a Matrix
problem link: https://www.deep-ml.com/problems/6
'''
import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

    eigenvalues, _ = np.linalg.eig(np.array(matrix, dtype=float))
    
    return eigenvalues