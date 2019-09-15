def main():
    print("function default arguments")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    avg = average_list_with_default(data)
    avg = average_list_with_default(data, 3)


def average_list_with_default(data, start=0, end=None, skip=None):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip)


def average_list(data, start, end, skip):
    if end is None:
        avg_data = data[start:]
    else:
        avg_data = data[start:end]

    sum = 0
    skip_count = 0
    for ind, num in enumerate(avg_data):
        if ind in skip:
            skip_count += 1
        else:
            sum += num
    dlen = len(avg_data) - skip_count
    average = sum / dlen
    print(f"average {start}~{end}, skip={skip} over {len(data)} numbers = {average}")
    return average


if __name__ == '__main__':
    main()
