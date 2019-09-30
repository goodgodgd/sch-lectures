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


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
avg = average_list(data, 2, 7, [4])

print("use keyword arguments")
avg = average_list(data, 2, 7, skip=[4])
avg = average_list(data, 2, end=7, skip=[4])
avg = average_list(data, start=2, end=7, skip=[4])
avg = average_list(data=data, start=2, end=7, skip=[4])

print("mix keyword arguments")
avg = average_list(data, start=2, end=7, skip=[4])
avg = average_list(data, end=7, start=2, skip=[4])
avg = average_list(data, skip=[4], start=2, end=7)


def average_list_with_default(data, start=0, end=None, skip=None):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip)


print("function default arguments")
avg = average_list_with_default(data)
avg = average_list_with_default(data, 3)
avg = average_list_with_default(data, end=5)
avg = average_list_with_default(data, skip=[3, 4])

def func(key, value, a={}):
    a[key] = value
    return a

print(func("a", 1))
print(func("b", 2))
