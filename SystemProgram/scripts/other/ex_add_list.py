
def test():
    num1 = [1, 2, 3]
    num2 = [4, 5, 6, 7, 8]
    result = add_lists(num1, num2)
    print(f"result: {num1} + {num2} = {result}")
    result = add_lists(num1, num2, shortlen=False)
    print(f"result: {num1} + {num2} = {result} with shortlen=False")
    result = add_lists(num1, num2, shortlen=False, start=1)
    print(f"result: {num1} + {num2} = {result} with shortlen=False, start=1")
    result = add_lists(num1, num2, shortlen=False, start=1, verbose=True)
    print(f"result: {num1} + {num2} = {result} with shortlen=False, start=1, verbose=True")


def add_lists(list1, list2, shortlen=True, start=0, verbose=False):
    # 함수 내부에서 list1, list2를 수정한 것이 함수 밖의 변수에
    # 영향을 미치지 않도록 내부에서 복사본 만들어 사용하기
    list1 = [v for v in list1]
    list2 = [v for v in list2]
    minlen = min(len(list1), len(list2))
    maxlen = max(len(list1), len(list2))

    if start > 0:
        list1 = list1[start:]
        list2 = list2[start:]

    if shortlen is True:
        list1 = list1[:minlen]
        list2 = list2[:minlen]
    else:
        for ind in range(minlen, maxlen):
            if len(list1) < maxlen:
                list1.append(0)
            if len(list2) < maxlen:
                list2.append(0)

    result = []
    for v1, v2 in zip(list1, list2):
        result.append(v1 + v2)

    if verbose is True:
        print(f"(verbose) {list1} + {list2} = {result}")

    return result


if __name__ == '__main__':
    test()

