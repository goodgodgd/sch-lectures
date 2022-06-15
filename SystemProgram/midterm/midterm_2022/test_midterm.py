from midterm_correct_answer import *

# ----------
text = "for the people by the people of the people"
result = count_words(text)
print("[count_words]", result)

# ----------
data = [1, 2, 3, 4, 5]
result = average_list_simple(data)
print("[average_list_simple]", result)

# ----------
data = [1, 2, 3, 4, 5]
result = average_list_complex(data)
print("[average_list_complex]", result)
result = average_list_complex(data, 1, 4)
print("[average_list_complex]", result)
result = average_list_complex(data, skip_values=[1, 2])
print("[average_list_complex]", result)

# ----------
foo = [1, 2, 3, 4, 5]
bar = [1, 2, 3, 4, 5]
result = add_two_lists(foo, bar)
print("[add_two_lists]", result)

# ----------
foo = {1: 1, 2: 2, 3: 3, 4: 4}
bar = {3: 1, 1: 3, 2: 2, 5: 5}
result = add_two_dicts(foo, bar)
print("[add_two_dicts]", result)

# ----------
text = "for the people by the people of the people"
srcfile = "__test__/sample.txt"
dstfile = "__test__/sample_revised.txt"
with open(srcfile, "w") as f:
    f.write(text)

replace_word_in_file(srcfile, "people", "python", dstfile)
with open(dstfile, "r") as f:
    text_revised = f.read()
print("[replace_word_in_file]", text_revised)

# ----------
rootpath = "__test__/testdir"
directories = ["apple", "banana"]
files = ["cherry.txt", "mango.txt"]
if os.path.isdir(rootpath):
    shutil.rmtree(rootpath)
os.mkdir(rootpath)
for dname in directories:
    os.mkdir(os.path.join(rootpath, dname))
for fname in files:
    with open(os.path.join(rootpath, fname), "w") as f:
        f.write(fname)

filemng = FileManager(rootpath)
print("[FileManager.__init__] self.items:", filemng.items)
filemng.make_dir("melon")
print("[FileManager.make_dir] make 'melon'")
print("[FileManager.get_dirs]", filemng.get_dirs())
filemng.remove_dir("apple")
print("[FileManager.remove_dir] remove 'apple'")
print("[FileManager.get_dirs]", filemng.get_dirs())
print("[FileManager.remove_file] remove 'cherry'")
filemng.remove_file("cherry.txt")
print("[FileManager.get_files]", filemng.get_files())

# ----------
data = [list(range(i*3, (i+1)*3)) for i in range(3)]
data = np.array(data)
print(data)
result = sum_array2d_column(data, 1)
print("[numpy_column_sum]", result)
result = sum_array2d_column(data, 5)

# ----------
python = np.array([[1, 2, 3], [7, 8, 9], [4, 5, 6]])
cpp = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])

cpp_high_python_mean, cpp_low_python_mean = score_correlation(python, cpp)
print("[score_correlation]", cpp_high_python_mean, cpp_low_python_mean)

