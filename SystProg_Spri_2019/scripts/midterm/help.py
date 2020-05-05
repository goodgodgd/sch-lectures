import numpy as np


def expect_results1():
    m1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])      # 3x4
    m2 = np.array([[1, 3, 5, 7], [2, 4, 6, 8], [9, 10, 11, 12]])      # 3x4
    m3 = np.array([[1, 3, 5], [7, 2, 4], [6, 8, 9], [10, 11, 12]])    # 3x4
    m1.dot(m2)
    m4 = m1.dot(m3)
    print(m4)
    m4 = m4.tolist()
    print(m4)
    assert m4 == [[73, 75, 88], [169, 171, 208], [265, 267, 328]]


def expect_results2():
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[1, 2], [3, 4]])
    m4 = m1.dot(m2)
    print(m4)
    m4 = m4.tolist()
    print(m4)
    assert m4 == [[7, 10], [15, 22]]


expect_results1()
expect_results2()
