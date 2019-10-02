import matrix.dense_matrix as dm
import matrix.sparse_matrix as sm

print("="*30 + "\nProblem 1")
dm1 = [[1, 2], [3, 4], [5, 6]]
dm2 = [[1, 2], [3, 4]]

res = dm.add(dm1[:2], dm2)
print("add:", res)
res = dm.multiply(dm1, dm2)
print("multiply:", res)


print("="*30 + "\nProblem 2")
sm1 = {'rows': 3, 'cols': 3, '00': 1, '11': 2, '22': 3}
sm2 = {'rows': 3, 'cols': 3, '01': 1, '11': 2, '21': 3}
res = sm.add(sm1, sm2)
print("add:", res)
res = sm.dense(res)
print("dense:", res)


def example(num):
    if num > 10:
        raise Exception("number > 10")


try:
    example(11)
except Exception as ex:
    print("[Exception]", ex)


print("="*30 + "\nProblem 3")
dm1 = [[1, 2], [3, 4], [6]]
dm2 = [[1, 2], [3, 4]]
dm3 = [[1, 2]]

try:
    res = dm.add_handle_exception(dm2, dm3)
except Exception as ex:
    print("[Exception] 1:", ex)

try:
    res = dm.add_handle_exception(dm1, dm2)
except Exception as ex:
    print("[Exception] 2:", ex)

try:
    res = dm.multiply_handle_exception(dm2, dm3)
except Exception as ex:
    print("[Exception] 3:", ex)

try:
    res = dm.multiply_handle_exception(dm1, dm2)
except Exception as ex:
    print("[Exception] 4:", ex)


sm1 = {'rows': 3, '00': 1, '11': 2, '22': 3, '33': 4}
sm2 = {'rows': 3, 'cols': 2, '00': 1, '11': 2, '22': 3}
sm3 = {'rows': 3, 'cols': 2, '00': 1, '11': 2}
sm4 = {'rows': 3, 'cols': 3, '01': 1, '11': 2, '21': 3}

try:
    res = sm.add_handle_exception(sm1, sm2)
except Exception as ex:
    print("[Exception] 5:", ex)

try:
    res = sm.add_handle_exception(sm2, sm4)
except Exception as ex:
    print("[Exception] 6:", ex)

try:
    res = sm.add_handle_exception(sm3, sm4)
except Exception as ex:
    print("[Exception] 7:", ex)

try:
    res = sm.dense_handle_exception(sm1)
except Exception as ex:
    print("[Exception] 8:", ex)

try:
    res = sm.dense_handle_exception(sm2)
except Exception as ex:
    print("[Exception] 9:", ex)
