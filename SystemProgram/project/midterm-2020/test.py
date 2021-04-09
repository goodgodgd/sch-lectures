import os
import shutil
from matrix import Matrix
import matrix_file as mf


def test_matrix():
    test_row_size_error()
    test_add_size_error()
    test_mul_size_error()
    test_add_result()
    test_mul_result()
    test_read_write()
    test_write_anywhere()
    # 테스트 케이스 추가


def test_row_size_error():
    print("test_row_size_error: 각 행의 길이 검사를 하는지 확인")
    t1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    t2 = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
    t3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
    t4 = [[1, 2], [5, 6, 7], [9, 10, 11, 12]]

    def create_mat(data):
        m = Matrix(data)

    # 에러가 나지 않아야 하는 케이스
    create_mat(t1)
    create_mat(t2)
    # 에러가 나야하는 케이스
    supposed_to_make_error(create_mat, t3)
    supposed_to_make_error(create_mat, t4)
    print("!!! test_row_size_error passed")


def test_add_size_error():
    print("test_add_size_error: 두 행렬이 더해질 수 있는 크기의 행렬인지 확인하는지를 확인")
    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 3x4
    m2 = Matrix([[9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]])  # 3x4
    m3 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])  # 2x4
    m4 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # 4x3

    def add_mat(ma, mb):
        mat = ma + mb

    # 에러가 나지 않아야 하는 케이스
    add_mat(m1, m1)
    add_mat(m1, m2)
    # 에러가 나야하는 케이스
    supposed_to_make_error(add_mat, m1, m3)
    supposed_to_make_error(add_mat, m1, m4)
    supposed_to_make_error(add_mat, m2, m4)
    print("!!! test_add_size_error passed")


def test_mul_size_error():
    print("test_mul_size_error: 두 행렬이 곱해질 수 있는 크기의 행렬인지 확인하는지를 확인")
    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 3x4
    m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # 4x3
    m3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 3x3
    m4 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])  # 2x4

    def mul_mat(ma, mb):
        mat = ma * mb

    # 에러가 나지 않아야 하는 케이스
    mul_mat(m1, m2)
    mul_mat(m3, m3)
    # 에러가 나야하는 케이스
    supposed_to_make_error(mul_mat, m1, m3)
    supposed_to_make_error(mul_mat, m2, m4)
    supposed_to_make_error(mul_mat, m3, m4)
    print("!!! test_mul_size_error passed")


def test_add_result():
    print("test_add_result: 두 행렬을 더한 값이 맞는지 확인")
    m1 = Matrix([[1, 2], [3, 4]])  # 2x2
    m2 = Matrix([[1, 2], [3, 4]])  # 2x2
    m3 = m1 + m2
    # 두 개가 같아야 에러 없이 통과
    assert m3.data == [[2, 4], [6, 8]]

    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 3x4
    m2 = Matrix([[1, 3, 5, 7], [2, 4, 6, 8], [9, 10, 11, 12]])  # 3x4
    m3 = m1 + m2
    # 두 개가 같아야 에러 없이 통과
    assert m3.data == [[2, 5, 8, 11], [7, 10, 13, 16], [18, 20, 22, 24]]
    print("!!! test_add_result passed")


def test_mul_result():
    print("test_mul_result: 두 행렬을 곱한 값이 맞는지 확인")
    m1 = Matrix([[1, 2], [3, 4]])  # 2x2
    m2 = Matrix([[1, 2], [3, 4]])  # 2x2
    m3 = m1 * m2
    # 두 개가 같아야 에러 없이 통과
    assert m3.data == [[7, 10], [15, 22]]

    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 3x4
    m2 = Matrix([[1, 3, 5], [7, 2, 4], [6, 8, 9], [10, 11, 12]])  # 4x3
    m3 = m1 * m2
    # 두 개가 같아야 에러 없이 통과
    assert m3.data == [[73, 75, 88], [169, 171, 208], [265, 267, 328]]
    print("!!! test_mul_result passed")


def test_read_write():
    print("test_read_write: 행렬을 파일출력 후 다시 읽었을때 같은 값의 행렬이 나오는지 확인")
    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 3x4
    m2 = Matrix([[1, 3, 5], [7, 2, 4], [6, 8, 9], [10, 11, 12]])  # 4x3
    m3 = m1 * m2
    # 일단 현재 경로에서 파일 입출력 기능만 확인
    savedir = os.path.dirname(os.path.abspath(__file__))
    mf.write_matrix(m1, os.path.join(savedir, "m1.mat"))
    mf.write_matrix(m2, os.path.join(savedir, "m2.mat"))
    mf.write_matrix(m3, os.path.join(savedir, "m3.mat"))

    m1_read = mf.read_matrix(os.path.join(savedir, "m1.mat"))
    assert m1.data == m1_read.data

    mats = mf.read_all_matrices(savedir)
    assert m2.data == mats[1].data
    assert m3.data == mats[2].data
    print("!!! test_read_write passed")


def test_write_anywhere():
    print("test_write_anywhere: 행렬을 임의의 경로에 만들 수 있는지 확인")
    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 3x4
    savedir = "C:\\mat987\\data135"
    # 혹시라도 경로가 존재하면 미리 삭제
    shutil.rmtree(savedir, ignore_errors=True)
    mf.write_matrix(m1, os.path.join(savedir, "m1.mat"))
    print("!!! test_write_anywhere passed")


def supposed_to_make_error(func, *args):
    """
    func(*args)를 실행하여 ValueError가 발생해야만 정상적으로 코드가 작동함
    ValueError가 발생하지 않으면 에러 발생하여 코드 종료
    """
    try:
        func(*args)
    except ValueError as ve:
        print(ve)

        return
    assert False


# --------------------------------------------------
# 테스트 함수 여기에 추가


if __name__ == "__main__":
    test_matrix()
