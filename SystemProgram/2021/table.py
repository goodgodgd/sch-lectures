class Table:
    def __init__(self, data):
        self.data = data
        self.rows, self.cols = self.check_size()

    def __str__(self):
        """
        Table을 문자열로 변환하여 리턴, 한 column은 기본 5칸 차지
        e.g. df = Table({"kim": [1, 2, 3], "lee": [4, 5, 6]})
        print(df)
        kim  lee
        1    4
        2    5
        3    6
        """
        result = ""
        for key in self.data:
            result += f"{key:5}"
        result += "\n"
        for i in range(self.rows):
            for key in self.data:
                result += f"{self.data[key][i]:<5}"
            result += "\n"
        return result

    def check_size(self):
        """
        data가 Table이 될 수 있는지 확인
        예를 들어 {"kim": [1, 2, 3], "lee": [4, 5, 6]}는 3x2 표가 될 수 있지만
        {"kim": [1, 2, 3], "lee": [4, 5]}는 표가 될 수 없다.
        표가 될 수 없으면 다음과 같이 에러내기: raise ValueError("different row sizes")
        표가 될 수 있으면 행의 개수, 열의 개수 리턴
        """
        cols = len(self.data)
        rows = None
        for key, column in self.data.items():
            cur_rows = len(column)
            if rows is None:
                rows = cur_rows
            elif rows != cur_rows:
                raise ValueError("different row sizes")
        return rows, cols

    def __add__(self, other):
        """
        '+' 연산자 오버로딩: __add__() 구현하면 C = A+B 실행시 작동
        self.data와 other.data를 더한 새로운 Table 객체 만들어 반환
        """
        self.check_column_titles(other)
        self.check_add_sizes(other)
        new_data = dict()
        for key in self.data:
            new_col = [a + b for a, b in zip(self.data[key], other.data[key])]
            new_data[key] = new_col
        return Table(new_data)

    def check_column_titles(self, other):
        """
        self.data와 other.data의 column title(dict key)이 같은지 확인하고
        아니면 다음과 같이 에러내기: raise ValueError("different column titles")
        주의: column title의 순서는 상관없음
        """
        mykeys = list(self.data.keys())
        mykeys.sort()
        otkeys = list(other.data.keys())
        otkeys.sort()
        if mykeys != otkeys:
            raise ValueError("different column titles")

    def check_add_sizes(self, other):
        """
        self.data와 other.data가 같은 크기의 표인지 확인하고
        아니면 다음과 같이 에러내기: raise ValueError("different matrix sizes")
        """
        if (self.rows != other.rows) or (self.cols != other.cols):
            raise ValueError("different matrix sizes")

    def append(self, new_row):
        """
        표에 행을 추가하기
        예를 들어 self.data={"kim": [1, 2, 3], "lee": [4, 5, 6]} 일 때
        입력으로 new_row={"kim": 10, "lee": 11}을 입력하면
        self.data={"kim": [1, 2, 3, 10], "lee": [4, 5, 6, 11]}
        """
        self.check_column_names(new_row)
        for key in self.data:
            self.data[key].append(new_row[key])
        self.rows, self.cols = self.check_size()

    def check_column_names(self, new_row):
        """
        check_column_titles()와 같은 역할인데 입력이 dict
        self.data의 key와 row_row의 key가 다르면 에러내기: raise ValueError("different column names")
        """
        mykeys = list(self.data.keys())
        mykeys.sort()
        otkeys = list(new_row.keys())
        otkeys.sort()
        if mykeys != otkeys:
            raise ValueError("different column names")

    def sum_vertically(self):
        """
        표를 세로로 더한 합계 구하기
        예를 들어 self.data={"kim": [1, 2, 3], "lee": [4, 5, 6]} 이면
        결과는 {"kim": 6, "lee", 15}
        """
        result = {key: sum(column) for key, column in self.data.items()}
        return result

    def sum_horizontally(self):
        """
        표를 가로로 더한 합계 구하기
        예를 들어 self.data={"kim": [1, 2, 3], "lee": [4, 5, 6]} 이면
        결과는 [5, 7, 9]
        """
        result = [0] * self.rows
        for key, column in self.data.items():
            for i, value in enumerate(column):
                result[i] += value
        return result

    def write(self, filename):
        """
        filename 경로에 파일 만들어서 self.data 기록하기
        e.g. filename="D:/mydir/myfile.txt"
        Hint: f"{self.data}"
        파일을 만들기 전에 파일을 만들고자 하는 폴더가 존재하는지 확인하고 없으면
        raise ValueError("cannot open a file in a non-existing directory")
        """
        import os
        if not os.path.isdir(os.path.dirname(filename)):
            raise ValueError("cannot open a file in a non-existing directory")
        with open(filename, "w") as f:
            f.write(f"{self.data}")

    @staticmethod
    def read(filename):
        """
        filename 경로의 파일 읽어서 새로운 Table 객체 리턴하기
        파일을 읽기 전에 파일이 존재하는지 확인하고 없으면
        raise ValueError("cannot open a non-existing file")
        Hint: eval("{'kim': [1, 2], 'lee': [3, 4]}")
        """
        import os
        if not os.path.isfile(filename):
            raise ValueError("cannot open a non-existing file")
        with open(filename, "r") as f:
            data = f.read()
        data = eval(data)
        return Table(data)



