import sys
import inspect
import os
import shutil
import numpy as np
import copy
import pandas as pd
from glob import glob
import importlib

import midterm_correct_answer as midcor
import __submitted__.JHW17 as midsub

DST_PATH = "C:/Users/SCH/Desktop"


def evaluate_main():
    global midsub
    set_print_options()

    score_table = pd.DataFrame()
    module_list = glob("./__submitted__/*.py")
    module_list.remove(os.path.join("./__submitted__", "midterm.py"))
    module_list = [mod.strip("./").strip(".py").replace("\\", ".") for mod in module_list]
    print("submitted module list:", module_list)

    # list of classes in this module
    eval_classes = [cls_type for name, cls_type in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(cls_type)]
    eval_classes.remove(EvalTemplate)
    print("evaluation class list:", eval_classes)

    for module in module_list:
        print("\n\n" + "#"*30 + "\n" + "MODULE:", module)
        midsub = importlib.import_module(module)
        person_scores = {}
        for cls_type in eval_classes:
            print("~"*10, "Test", cls_type.__name__, "~"*10)
            eval_obj = cls_type()
            person_scores[eval_obj.target_name] = eval_obj.evaluate()
        person_scores["total"] = sum(list(person_scores.values()))
        person_scores["name"] = module.split(".")[1]
        score_table = score_table.append(person_scores, ignore_index=True)
        print("score table\n", score_table)

    print("="*30)
    print("person_scores:", person_scores)
    print("score_table:", score_table)
    score_table.to_csv(os.path.join(DST_PATH, "systprog_eval.csv"), index=False)


def set_print_options():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 3)


class EvalTemplate:
    def __init__(self):
        self.target_name = ""
        self.scores = {}
        self.results = {}

    def run(self, module):
        pass

    def try_run(self, func, test_key=None):
        try:
            f_res = func()
            if test_key:
                self.results[test_key] = f_res
        except Exception as e:
            print("Exception:", e)
            return 0
        return 1

    def evaluate(self):
        expected = copy.deepcopy(self.run(midcor))
        result = copy.deepcopy(self.run(midsub))
        print(f"  expected result: ", expected)
        print(f"  submitted result:", result)
        score_sum = 0
        assert list(self.scores.keys()) == list(expected.keys())

        for test_key in self.scores:
            if test_key in result and expected[test_key] == result[test_key]:
                score_sum += self.scores[test_key]
                print(f"  {self.target_name}/{test_key} scored {self.scores[test_key]}")
            else:
                print(f">>{self.target_name}/{test_key} FAILED")
                if test_key in result:
                    print(f"\tcompare: /{expected[test_key]}/{result[test_key]}/")
        print(f"{self.target_name} scored {score_sum}")
        return score_sum


class EvalCountWords(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "count_words"
        self.scores = {"basic": 4, "applied": 4}

    def run(self, module):
        self.results = {}
        text = "for the people by the people of the people"
        f = (lambda: module.count_words(text))
        self.try_run(f, "basic")
        text = "나는 너를 좋아하고 너를 좋아하고 너도 나를 좋아하고 나를 좋아하고 " \
               "우린 서로 좋아하는데도 그 누구도 말을 안 해요"
        f = (lambda: module.count_words(text))
        self.try_run(f, "applied")
        return self.results


class EvalAverageListSimple(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "average_simple"
        self.scores = {"basic": 4, "applied": 4}
        self.data = np.random.rand(8).round(3).tolist()
        print("data to average:", self.data)

    def run(self, module):
        self.results = {}
        data = [1, 2, 3, 4, 5]
        f = (lambda: module.average_list_simple(data))
        self.try_run(f, "basic")
        f = (lambda: module.average_list_simple(self.data))
        self.try_run(f, "applied")
        return self.results


class EvalAverageListComplex(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "average_complex"
        self.scores = {"basic": 4, "startend": 4, "skipval": 4}
        self.data = np.random.rand(8).round(3).tolist()
        print("data to average:", self.data)

    def run(self, module):
        self.results = {}
        data = [1, 2, 3, 4, 5]
        f = (lambda: module.average_list_complex(data))
        self.try_run(f, "basic")
        f = (lambda: module.average_list_complex(self.data, 1, 6))
        self.try_run(f, "startend")
        f = (lambda: module.average_list_complex(data, skip_values=[2, 4]))
        self.try_run(f, "skipval")
        return self.results


class EvalAddLists(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "add_lists"
        self.scores = {"basic": 4, "applied": 4}
        self.data1 = np.random.rand(8).round(3).tolist()
        self.data2 = np.random.rand(8).round(3).tolist()
        print("data to add lists:", self.data1, self.data2)

    def run(self, module):
        self.results = {}
        foo = [1, 2, 3, 4, 5]
        bar = [1, 2, 3, 4, 5]
        f = (lambda: module.add_two_lists(foo, bar))
        self.try_run(f, "basic")
        f = (lambda: module.add_two_lists(self.data1, self.data2))
        self.try_run(f, "applied")
        return self.results


class EvalAddDicts(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "add_dicts"
        self.scores = {"basic": 6, "applied": 6}
        self.data1 = dict(zip(["foo", "bar", "goo", "qux", 1, 2, 3, 4], np.random.rand(8).round(3).tolist()))
        self.data2 = dict(zip(["foo", "bar", "goo", "qux", 1, 2, 3, 4], np.random.rand(8).round(3).tolist()))
        print("data to add dicts:", self.data1, self.data2)

    def run(self, module):
        self.results = {}
        foo = {1: 1, 2: 2, 3: 3, 4: 4}
        bar = {3: 1, 1: 3, 2: 2, 5: 5}
        f = (lambda: module.add_two_dicts(foo, bar))
        self.try_run(f, "basic")
        f = (lambda: module.add_two_dicts(self.data1, self.data2))
        self.try_run(f, "applied")
        return self.results


class EvalReplaceWord(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "replace_word"
        self.scores = {"basic": 5, "applied": 5}

    def run(self, module):
        self.results = {}
        srcfile = "__test__/sample.txt"
        dstfile = "__test__/sample_revised.txt"
        text = "for the people by the people of the people"
        with open(srcfile, "w") as f:
            f.write(text)
        f = (lambda: module.replace_word_in_file(srcfile, "people", "python", dstfile))
        if self.try_run(f):
            with open(dstfile, "r") as f:
                self.results["basic"] = f.read().strip()

        text = "산토끼 토끼야 어디를 가느냐?"
        with open(srcfile, "w") as f:
            f.write(text)
        f = (lambda: module.replace_word_in_file(srcfile, "토끼", "딸기", dstfile))
        if self.try_run(f):
            with open(dstfile, "r") as f:
                self.results["applied"] = f.read().strip()

        return self.results


class EvalFileManager(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "file_manager"
        self.scores = {"init_items": 4, "init_files": 4, "init_dirs": 4,
                       "make_dir": 4, "remove_dir": 4, "remove_file": 4}

    def run(self, module):
        self.results = {}
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

        try:
            filemng = module.FileManager(rootpath)
        except Exception as e:
            print("Exception:", e)
            return {}
        f = (lambda: filemng.items)
        self.try_run(f, "init_items")
        f = (lambda: filemng.get_files())
        self.try_run(f, "init_files")
        f = (lambda: filemng.get_dirs())
        self.try_run(f, "init_dirs")

        f = (lambda: filemng.make_dir("melon"))
        self.try_run(f)
        file_correct = midcor.FileManager(rootpath)
        f = (lambda: file_correct.get_dirs())
        self.try_run(f, "make_dir")

        f = (lambda: filemng.remove_dir("apple"))
        self.try_run(f)
        file_correct = midcor.FileManager(rootpath)
        f = (lambda: file_correct.get_dirs())
        self.try_run(f, "remove_dir")

        f = (lambda: filemng.remove_file("cherry.txt"))
        self.try_run(f)
        file_correct = midcor.FileManager(rootpath)
        f = (lambda: file_correct.get_files())
        self.try_run(f, "remove_file")

        return self.results


class EvalSum2D(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "sum_array2d"
        self.scores = {"d1col1": 2, "d1col5": 2, "d2col2": 2, "d2col8": 2}
        self.data = np.random.rand(4, 3).round(3)
        print("data to sum:", self.data)

    def run(self, module):
        self.results = {}
        data = [list(range(i * 3, (i + 1) * 3)) for i in range(3)]
        data = np.array(data)
        f = (lambda: module.sum_array2d_column(data, 1))
        self.try_run(f, "d1col1")
        f = (lambda: module.sum_array2d_column(data, 5))
        self.try_run(f, "d1col5")
        f = (lambda: module.sum_array2d_column(data, 2))
        self.try_run(f, "d2col2")
        f = (lambda: module.sum_array2d_column(data, 8))
        self.try_run(f, "d2col8")
        return self.results


class EvalCorrelation(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "correlation"
        self.scores = {"python_cpp": 4, "java_csh": 4}
        self.java = np.random.rand(4, 3).round(3)
        self.csharp = np.random.rand(4, 3).round(3)
        print("correlation data:", self.java, self.csharp)

    def run(self, module):
        self.results = {}
        python = np.array([[1, 2, 3], [7, 8, 9], [4, 5, 6]])
        cpp = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
        f = (lambda: module.score_correlation(python, cpp))
        self.try_run(f, "python_cpp")
        f = (lambda: module.score_correlation(self.java, self.csharp))
        self.try_run(f, "java_csh")
        return self.results


if __name__ == "__main__":
    evaluate_main()
