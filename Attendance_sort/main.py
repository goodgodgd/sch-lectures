import pandas as pd

FILES = ["D:/Naver MYBOX/동기화문서/강의자료/_2021-2 선형시스템/성적/선형시스템(11003) 출석부.csv",
         "D:/Naver MYBOX/동기화문서/강의자료/_2021-2 제어공학2/성적/제어공학2(11027) 출석부.csv",
         "D:/Naver MYBOX/동기화문서/강의자료/_2021-2 로봇공학/성적/로봇공학(11008) 출석부.csv"]


def sort_odd_even():
    for file in FILES:
        sort_impl(file)


def sort_impl(file):
    print("file", file)
    data = pd.read_csv(file)
    data["학번"] = data["학번"].astype('Int64')
    odd = data.loc[data["학번"] % 2 == 1, ["이름", "학번"]]
    odd["구분"] = "홀수"
    even = data.loc[data["학번"] % 2 == 0, ["이름", "학번"]]
    even["구분"] = "짝수"
    print("odd numbers", odd.head())
    print("even numbers", even.head())
    sorted = pd.concat([odd, even], axis=0)
    sorted.to_csv(file.replace("출석부.csv", "홀짝 출석부.csv"), index=False, encoding="cp949")


if __name__ == '__main__':
    sort_odd_even()
