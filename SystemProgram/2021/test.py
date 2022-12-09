import os
from table import Table


def test_matrix():
    test_row_size_error()
    test_print()
    test_add_size_error()
    test_add_result()
    test_append()
    test_sum_vertically()
    test_sum_horizontally()
    test_write()
    test_read()


def test_row_size_error():
    print("=== test_row_size_error: 각 열의 길이가 같은지 확인")
    t1 = {"kim": [1, 2, 3, 4], "lee": [5, 6, 7, 8], "park": [9, 10, 11, 12]}
    t2 = {"jone": [1, 2, 3], "kane": [5, 6, 7], "eric": [9, 10, 11]}
    t3 = {"sys": [1, 2, 3, 4], "tem": [5, 6, 7, 8], "prog": [9, 10, 11]}
    t4 = {"choi": [1, 2], "hyuk": [5, 6, 7], "doo": [9, 10, 11, 12]}

    def create_mat(data):
        m = Table(data)

    # 에러가 나지 않아야 하는 케이스
    create_mat(t1)
    create_mat(t2)
    # 에러가 나야하는 케이스
    supposed_to_make_error(create_mat, t3)
    supposed_to_make_error(create_mat, t4)
    print("!!! test_row_size_error passed")


def test_print():
    print("=== test_print: 표를 표의 형태로 프린트")
    t1 = Table({"kim": [1, 2, 3], "lee": [5, 6, 7], "park": [9, 10, 11]})
    t2 = Table({"jone": [1, 2, 3, 4], "kane": [5, 6, 7, 8], "eric": [9, 10, 11, 12]})
    print(t1)
    print(t2)
    if str(t1) == "kim  lee  park \n1    5    9    \n2    6    10   \n3    7    11   \n":
        print("!!! test_print passed")
    else:
        print("!!! test_print may failed")


def test_add_size_error():
    print("=== test_add_size_error: 두 표가 더해질 수 있는지 확인")
    t1 = Table({"kim": [1, 2, 3], "lee": [5, 6, 7], "park": [9, 10, 11]})
    t2 = Table({"jone": [1, 2, 3], "kane": [5, 6, 7], "eric": [9, 10, 11]})
    t3 = Table({"kane": [1, 2, 3], "eric": [5, 6, 7], "jone": [9, 10, 11]})
    t4 = Table({"jone": [1, 2, 3, 4], "kane": [5, 6, 7, 8], "eric": [9, 10, 11, 12]})

    def add_tables(ma, mb):
        mat = ma + mb

    # 에러가 나지 않아야 하는 케이스
    add_tables(t2, t2)
    add_tables(t2, t3)
    # 에러가 나야하는 케이스
    supposed_to_make_error(add_tables, t1, t2)
    supposed_to_make_error(add_tables, t3, t4)
    print("!!! test_add_size_error passed")


def test_add_result():
    print("=== test_add_result: 두 표를 더한 값이 맞는지 확인")
    t1 = Table({"kim": [1, 2, 3, 4, 5], "lee": [6, 7, 8, 9, 10]})
    t2 = Table({"kim": [10, 9, 8, 7, 6], "lee": [5, 4, 3, 2, 1]})
    t3 = t1 + t2
    # 두 개가 같아야 에러 없이 통과
    assert t3.data == {"kim": [11, 11, 11, 11, 11], "lee": [11, 11, 11, 11, 11]}

    t1 = Table({"jone": [1, 2], "kane": [5, 6], "eric": [9, 10], "tom": [3, 7]})
    t2 = Table({"jone": [4, 3], "kane": [5, 7], "eric": [3, 8], "tom": [2, 1]})
    t3 = t1 + t2
    # 두 개가 같아야 에러 없이 통과
    assert t3.data == {"jone": [5, 5], "kane": [10, 13], "eric": [12, 18], "tom": [5, 8]}
    print("!!! test_add_result passed")


def test_append():
    print("=== test_append: 표에 행 추가")
    t1 = Table({"kim": [1, 2, 3], "lee": [5, 6, 7], "park": [9, 10, 11]})
    row1 = {"kim": 4, "lee": 8, "park": 12}
    row2 = {"kim": 4, "lee": 8, "jane": 12}

    def append_row(table, row):
        table.append(row)

    t1.append(row1)
    print("appended table:\n", t1)
    supposed_to_make_error(append_row, t1, row2)
    print("!!! test_append passed")


def test_sum_vertically():
    print("=== test_sum_vertically: 표의 세로 합계 구하기")
    t1 = Table({"kim": [1, 2, 3], "lee": [5, 6, 7], "park": [9, 10, 11]})
    result = t1.sum_vertically()
    print("test_sum_vertically:", result)
    assert result == {"kim": 6, "lee": 18, "park": 30}
    print("!!! test_sum_vertically passed")


def test_sum_horizontally():
    print("=== test_sum_horizontally: 표의 가로 합계 구하기")
    t1 = Table({"kim": [1, 2, 3], "lee": [5, 6, 7], "park": [9, 10, 11]})
    result = t1.sum_horizontally()
    print("sum_horizontally:", result)
    assert result == [15, 18, 21]
    print("!!! test_sum_horizontally passed")


# 시스템에 존재하는 경로
EXISTING_DIR = "D:/Work"
# 시스템에 존재하지 않는 경로
NON_EXISTING_DIR = "D:/haha"
T1 = Table({"kim": [1, 2, 3], "lee": [5, 6, 7], "park": [9, 10, 11]})


def test_write():
    print("=== test_write: 표를 파일에 저장")

    def write_file(table, filename):
        table.write(filename)

    filename = os.path.join(EXISTING_DIR, "table.txt")
    T1.write(filename)
    print("write a file", filename, "\n", T1)
    filename = os.path.join(NON_EXISTING_DIR, "table.txt")
    supposed_to_make_error(write_file, T1, filename)
    print("!!! test_write passed")


def test_read():
    print("=== test_read: 파일에서 표 읽어오기")

    def read_file(table, filename):
        table.read(filename)

    # test_write에서 만든 파일 경로
    filename = os.path.join(EXISTING_DIR, "table.txt")
    t2 = Table.read(filename)
    print("read a file", filename, "\n", t2)
    assert t2.data == T1.data
    # 시스템에 존재하지 않는 파일 경로
    filename = os.path.join(NON_EXISTING_DIR, "table.txt")
    supposed_to_make_error(read_file, Table, filename)

    print("!!! test_read passed")


def supposed_to_make_error(func, *args):
    """
    func(*args)를 실행하여 ValueError가 발생해야만 정상적으로 코드가 작동함
    ValueError가 발생하지 않으면 에러 발생시켜서 코드 종료
    """
    try:
        func(*args)
    except ValueError as ve:
        print("[supposed_to_make_error]", ve)

        return
    assert False


if __name__ == "__main__":
    test_matrix()
