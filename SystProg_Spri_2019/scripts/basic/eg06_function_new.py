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


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
avg = average_list(data, 2, 7, [4], True)

print("use keyword arguments")
avg = average_list(data, 2, 7, skip=[4], verbose=True)
avg = average_list(data, 2, end=7, skip=[4], verbose=True)
avg = average_list(data, start=2, end=7, skip=[4], verbose=True)
avg = average_list(data=data, start=2, end=7, skip=[4], verbose=True)

print("mix keyword arguments")
avg = average_list(data, start=2, end=7, skip=[4], verbose=True)
avg = average_list(data, end=7, start=2, skip=[4], verbose=True)
avg = average_list(data, skip=[4], start=2, end=7, verbose=True)


def average_list_with_default(data, start=0, end=None, skip=None, verbose=False):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip, verbose)


print("function default arguments")
avg = average_list_with_default(data)
print("average_list_with_default(data) =>", avg)
avg = average_list_with_default(data, 3)
print("average_list_with_default(data, 3) =>", avg)
avg = average_list_with_default(data, end=5)
print("average_list_with_default(data, end=5) =>", avg)
avg = average_list_with_default(data, skip=[3, 4])
print("average_list_with_default(data, skip=[3, 4]) =>", avg)


subject_scores = {"cpp": [57, 36, 80],
                  "java": [46, 88, 72],
                  "ruby": [85, 23, 34]}


def average_multi_subjects(scores, *args):
    averages = {}
    print("[average_multi_subjects] args:", args)
    print("[average_multi_subjects] *args:", *args)
    for subject in args:
        avg = average_list_with_default(scores[subject])
        print(f"average over {subject} scores: {avg:.1f}")
        averages[subject] = avg
    return averages


result = average_multi_subjects(subject_scores, "cpp")
result = average_multi_subjects(subject_scores, "cpp", "java", "ruby")
print("")


def average_variable_arguments(data, multiple, *args):
    # do some process ...
    data = [d*multiple for d in data]
    avg = average_list_with_default(data, *args)
    return avg


result = average_variable_arguments(data, 10, 1, 7)
print("average_variable_arguments(data, 1, 7) =>", result)
result = average_variable_arguments(data, 10, 1, 7, [3], False)
print("average_variable_arguments(data, 1, 7, [3], True) =>", result)
result = average_list_with_default(data, 1, 7)
print("average_list_with_default(data, 1, 7) =>", result)
result = average_list_with_default(data, 1, 7, [3], False)
print("average_list_with_default(data, 1, 7, [3], True) =>", result)
print("")


def average_keyworded_args(data, multiple, **kwargs):
    print("[average_subjects_varargs] kwargs:", kwargs)
    # do some process ...
    data = [d*multiple for d in data]
    avg = average_list_with_default(data, **kwargs)
    return avg


result = average_keyworded_args(data, 10, start=1, skip=[2, 3])
print("average_keyworded_args(data, start=1, skip=[2, 3]) =>", result)
result = average_keyworded_args(data, 10, start=1, end=7)
print("average_keyworded_args(data, start=1, end=7) =>", result)
print("")

subject_scores = {"cpp": [57, 36, 80, 53, 23],
                  "java": [46, 88, 72, 15, 54],
                  "ruby": [85, 23, 34, 91, 42]}


def average_subjects_kwargs(scores, multiple, *args, **kwargs):
    averages = {}
    for subject in args:
        data = [d*multiple for d in scores[subject]]
        avg = average_list_with_default(data, **kwargs)
        averages[subject] = avg
    return averages


result = average_subjects_kwargs(subject_scores, 10, "cpp", "java", start=1, end=4, skip=[2])
print("average_subjects_kwargs(subject_scores, 10, 'cpp', 'java', start=1, end=4, skip=[2]) =>", result)
print("")


print("variable scope")
if True:
    var_created = "created"
print("variable created inside block:", var_created)
if False:
    var_not_created = "not created"
try:
    print("variable NOT created inside block:", var_not_created)
except NameError as ne:
    print(ne)


global_var = 10
def add_ten_local():
    local_var = global_var + 10
    print("add_ten_local:", local_var)

def add_ten_global():
    try:
        global_var = global_var + 10
        print("add_ten_global:", global_var)
    except NameError as ne:
        print(ne)

def add_ten_global_two_steps():
    try:
        local_var = global_var + 10
        global_var = local_var
        print("add_ten_global_two_steps:", global_var)
    except NameError as ne:
        print(ne)

def add_ten_global_use_global():
    global global_var
    global_var = global_var + 10
    print("add_ten_global_use_global:", global_var)

add_ten_local()
add_ten_global()
add_ten_global_two_steps()
add_ten_global_use_global()
print("global_var=", global_var)

