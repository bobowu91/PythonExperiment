import numpy as np
from pytimer import process_time


@process_time
def imgRotate(n_dim, img):
    # create an empty nested list
    Matrix = [[0 for i in range(n_dim)] for j in range(n_dim)]
    # rotate a matrix by 90 degree clockwise
    for row_index in range(n_dim):
        for col_index in range(n_dim):
            Matrix[col_index][n_dim - row_index-1] = img[row_index][col_index]
    return Matrix


n_dim = 10
img = [np.random.choice(range(1, n_dim+5), n_dim, False) for i in range(n_dim)]
for i in img:
    print(i)

m = imgRotate(n_dim, img)
for i in m:
    print(i)
