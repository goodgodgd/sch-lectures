import os
import glob
from matrix import Matrix


def write_matrix(mat, filepath):
    """
    하나의 Matrix 객체를 파일로 저장하는 함수
    Hint: "f{mat}" 이용하면 쉽게 리스트를 문자열로 바꿀 수 있음
        os.makedirs() 함수를 이용하면 여러 단계의 경로를 쉽게 만들 수 있음
    :param mat: 저장할 행렬
    :param filepath: 저장할 파일명, 확장자 .mat으로 끝나야함
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(f"{mat}")


def read_matrix(filepath):
    """
    하나의 Matrix 객체를 파일에서 읽어오는 함수
    Hint: eval("[1, 2]")를 실행하면 숫자 리스트 [1, 2]가 출력됨
    :param filepath: 읽어올 파일 경로
    :return Matrix 객체 출력
    """
    with open(filepath, "r") as f:
        data = f.read()
        data = eval(data)
        mat = Matrix(data)
    return mat


def read_all_matrices(dirpath):
    """
    dirpath 경로 아래 있는 모든 .mat 파일을 찾아 Matrix 객체의 리스트 출력
    Hint: glob.glob과 read_matrix() 함수 이용
    :param dirpath: 파일들을 읽어들일 경로
    :return Matrix 객체 출력
    """
    files = glob.glob(os.path.join(dirpath, "*.mat"))
    matrices = []
    for file in files:
        mat = read_matrix(file)
        matrices.append(mat)
    return matrices

