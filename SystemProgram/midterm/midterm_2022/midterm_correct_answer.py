def count_words(text):
    words = text.split()
    words.sort()
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


def average_list_simple(data):
    return sum(data) / len(data)


def average_list_complex(data, start=None, end=None, skip_values=None):
    if end:
        data = data[:end]
    if start:
        data = data[start:]
    if skip_values:
        for val in skip_values:
            if val in data:
                data.remove(val)
    return sum(data) / len(data)


def add_two_lists(foo, bar):
    return [f+b for f, b in zip(foo, bar)]


def add_two_dicts(foo, bar):
    result = {}
    for key in foo:
        if key in bar:
            result[key] = foo[key] + bar[key]
    print(f"{foo} + {bar} = {result}")
    return result


def replace_word_in_file(srcfile, srcword, dstword, dstfile):
    with open(srcfile, 'r') as f:
        data = f.read()
        data = data.replace(srcword, dstword)

    with open(dstfile, 'w') as f:
        f.write(data)

import os
import glob
import shutil


class FileManager:
    def __init__(self, rootpath):
        self.rootpath = rootpath
        self.items = glob.glob(rootpath + "/*")

    def get_files(self):
        return [f for f in self.items if os.path.isfile(f)]

    def get_dirs(self):
        return [f for f in self.items if os.path.isdir(f)]

    def make_dir(self, dirname):
        if not os.path.isdir(os.path.join(self.rootpath, dirname)):
            os.mkdir(os.path.join(self.rootpath, dirname))
        self.items = glob.glob(self.rootpath + "/*")

    def remove_dir(self, dirname):
        if os.path.isdir(os.path.join(self.rootpath, dirname)):
            shutil.rmtree(os.path.join(self.rootpath, dirname))
        self.items = glob.glob(self.rootpath + "/*")

    def remove_file(self, filename):
        if os.path.isdir(os.path.join(self.rootpath, filename)):
            os.remove(os.path.join(self.rootpath, filename))
        self.items = glob.glob(self.rootpath + "/*")


import numpy as np


def sum_array2d_column(data, col):
    if col >= data.shape[1]:
        print("[sum_array2d_column] wrong column", col)
        return 0
    data = np.array(data)
    return np.sum(data[:, col])


def score_correlation(python, cpp):
    cpp_mean = np.mean(cpp)
    cpp_high_python_mean = np.mean(python[cpp >= cpp_mean])
    cpp_low_python_mean = np.mean(python[cpp < cpp_mean])
    return cpp_high_python_mean, cpp_low_python_mean
