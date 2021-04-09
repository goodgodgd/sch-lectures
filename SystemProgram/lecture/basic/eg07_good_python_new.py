def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = average_keyworded_args(data, 10, start=1, skip=[2, 3])
    print("average_keyworded_args(data, start=1, skip=[2, 3]) =>", result)
    result = average_keyworded_args(data, 10, start=1, end=7)
    print("average_keyworded_args(data, start=1, end=7) =>", result)


def average_keyworded_args(data, multiple, **kwargs):
    data = [d*multiple for d in data]
    avg = average_list_with_default(data, **kwargs)
    return avg


def average_list_with_default(data, start=0, end=None, skip=None, verbose=False):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip, verbose)


def average_list(data, start, end, skip, verbose):
    if end is None:
        avg_data = data[start:]
    else:
        avg_data = data[start:end]

    sum = 0
    for ind, num in enumerate(avg_data):
        if ind not in skip:
            sum += num
    dlen = len(avg_data) - len(skip)
    average = sum / dlen
    if verbose:
        print(f"average {start}~{end} with skipping {skip} = {average}")
    return average


if __name__ == '__main__':
    main()
