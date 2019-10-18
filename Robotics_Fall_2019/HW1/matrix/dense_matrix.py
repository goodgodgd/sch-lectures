
def add(m1, m2):
    h1, w1 = (len(m1), len(m1[0]))
    result = [[0 for i in range(w1)] for k in range(h1)]
    for row in range(h1):
        for col in range(w1):
            result[row][col] = m1[row][col] + m2[row][col]
    return result


def multiply(m1, m2):
    h1, w1 = (len(m1), len(m1[0]))
    h2, w2 = (len(m2), len(m2[0]))
    result = [[0 for i in range(w2)] for k in range(h1)]
    for row in range(h1):
        for col in range(w2):
            for i in range(w1):
                result[row][col] += m1[row][i] * m2[i][col]
    return result


def add_handle_exception(m1, m2):
    check_consistent_cols(m1)
    check_consistent_cols(m2)
    h1, w1 = (len(m1), len(m1[0]))
    h2, w2 = (len(m2), len(m2[0]))
    if h1 != h2 or w1 != w2:
        raise Exception("different matrix size")

    result = [[0 for i in range(w1)] for k in range(h1)]
    for row in range(h1):
        for col in range(w1):
            result[row][col] = m1[row][col] + m2[row][col]
    return result


def multiply_handle_exception(m1, m2):
    check_consistent_cols(m1)
    check_consistent_cols(m2)
    h1, w1 = (len(m1), len(m1[0]))
    h2, w2 = (len(m2), len(m2[0]))
    if w1 != h2:
        raise Exception(f"cannot multiply ({h1},{w1}) x ({h2},{w2})")

    result = [[0 for i in range(w2)] for k in range(h1)]
    for row in range(h1):
        for col in range(w2):
            for i in range(w1):
                result[row][col] += m1[row][i] * m2[i][col]
    return result


def check_consistent_cols(mat):
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise Exception("matrix columns are not consistent")
