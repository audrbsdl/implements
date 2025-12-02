'''
Calculate Covariance Matrix
problem link: https://www.deep-ml.com/problems/10
'''
import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	
    vectors = np.array(vectors)
    covs = np.cov(vectors, bias=False)

	return covs.tolist()