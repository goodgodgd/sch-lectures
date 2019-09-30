
def add(m1, m2):
    h1, w1 = (m1['rows'], m1['cols'])
    result = {'rows': h1, 'cols': w1}
    add_values(result, m1)
    add_values(result, m2)
    return result


def add_values(dst, src):
    for key, value in src.items():
        if key == 'rows' or key == 'cols':
            continue
        if key in dst:
            dst[key] += value
        else:
            dst[key] = value


def dense(sparse):
    h1, w1 = (sparse['rows'], sparse['cols'])
    result = [[0 for i in range(w1)] for k in range(h1)]
    for row in range(h1):
        for col in range(w1):
            key = f'{row}{col}'
            if key in sparse:
                result[row][col] = sparse[key]
    return result


def add_handle_exception(m1, m2):
    if 'rows' not in m1 or 'cols' not in m1:
        raise Exception("either 'rows' or 'cols' is not in keys")
    if 'rows' not in m2 or 'cols' not in m2:
        raise Exception("either 'rows' or 'cols' is not in keys")
    check_indices(m1)
    check_indices(m2)
    h1, w1 = (m1['rows'], m1['cols'])
    h2, w2 = (m2['rows'], m2['cols'])
    if h1 != h2 or w1 != w2:
        raise Exception("different matrix size")

    result = {'rows': h1, 'cols': w1}
    add_values(result, m1)
    add_values(result, m2)
    return result


def dense_handle_exception(sparse):
    if 'rows' not in sparse or 'cols' not in sparse:
        raise Exception("either 'rows' or 'cols' is not in keys")
    check_indices(sparse)
    h1, w1 = (sparse['rows'], sparse['cols'])
    result = [[0 for i in range(w1)] for k in range(h1)]
    for row in range(h1):
        for col in range(w1):
            key = f'{row}{col}'
            if key in sparse:
                result[row][col] = sparse[key]
    return result


def check_indices(sparse):
    height, width = (sparse['rows'], sparse['cols'])
    for key, value in sparse.items():
        if key == 'rows' or key == 'cols':
            continue
        row = int(key[0])
        col = int(key[1])
        if row >= height or col >= width:
            raise Exception("index out of bound")


