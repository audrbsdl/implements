'''
Matrix-Vector Dot Product
problem link: https://www.deep-ml.com/problems/1
'''

def matrix_dot_vector(matrix: list[list[int|float]], vector: list[int|float]) -> list[int|float]:
    if len(matrix[0]) != len(vector):
        return -1
    
    result = []
    for row in matrix:
        s = 0
        for a, b in zip(row, vector):
            s += a * b
        result.append(s)

    return result
