import numpy as np

def reshape_matrix(matrix: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    try:
        reshaped_matrix = np.array(matrix).reshape(new_shape)
    except ValueError:
        return []
    return reshaped_matrix.tolist()