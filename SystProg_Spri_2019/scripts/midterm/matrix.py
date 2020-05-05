class Matrix:
    def __init__(self, data):
        rows, cols = self.check_size(data)
        self.data = data
        self.rows = rows
        self.cols = cols

    def __str__(self):
        return f"{self.data}"

    def check_size(self, data):
        """
        data가 행렬이 될 수 있는지 확인
        예를 들어 [[1, 2, 3], [4, 5, 6]]는 2x3 행렬이 될 수 있지만
        [[1, 2, 3], [4, 5]]는 행렬이 될 수 없다.
        행렬이 될 수 없으면 다음과 같이 에러내기: raise ValueError("different row sizes")
        행렬이 될 수 있으면 행의 개수, 열의 개수 출력
        """
        rows = len(data)
        cols = len(data[0])
        for row in data:
            if len(row) != cols:
                raise ValueError("different row sizes")
        return rows, cols

    def __add__(self, other):
        """
        '+' 연산자 오버로딩: __add__() 구현하면 C = A+B 실행시 작동
        self.data와 other.data를 더한 새로운 Matrix 객체 output 만들어 반환
        """
        self.check_add_sizes(other)
        output = []
        for r in range(self.rows):
            newrow = []
            for c in range(self.cols):
                value = self.data[r][c] + other.data[r][c]
                newrow.append(value)
            output.append(newrow)
        output = Matrix(output)
        return output

    def check_add_sizes(self, other):
        """
        self.data와 other.data가 더해질 수 있는 사이즈의 행렬인지 확인하고
        아니면 다음과 같이 에러내기: raise ValueError("different matrix sizes")
        """
        if (self.rows != other.rows) or (self.cols != other.cols):
            raise ValueError("different matrix sizes")

    def __mul__(self, other):
        """
        '*' 연산자 오버로딩: __sub__() 구현하면 C = A * B 실행시 작동
        self.data와 other.data를 곱한 새로운 Matrix 객체 output 만들어 반환
        """
        self.check_mul_sizes(other)
        output = []
        for r in range(self.rows):
            newrow = []
            for c in range(other.cols):
                value = 0
                for k in range(self.cols):
                    value += self.data[r][k] * other.data[k][c]
                newrow.append(value)
            output.append(newrow)
        output = Matrix(output)
        return output

    def check_mul_sizes(self, other):
        """
        self.data 와 other.data 가 곱해질 수 있는 사이즈의 행렬인지 확인하고
        아니면 다음과 같이 에러내기: raise ValueError("not able to multiply")
        """
        if self.cols != other.rows:
            raise ValueError("not able to multiply")
