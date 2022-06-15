import sys
import os
import shutil
import numpy as np

submit_path = "D:/work/systprog/submitted"
if submit_path not in sys.path:
    sys.path.append(submit_path)

import midterm_correct_answer as midcor
import KSR08 as midsub


class EvalTemplate:
    def __init__(self):
        self.target_name = ""
        self.scores = {}
        print("-"*30)

    def run(self, module):
        pass

    def try_run(self, func, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print("Exception:", e)
            return None
        return result

    def evaluate(self):
        expected = self.run(midcor)
        result = self.run(midsub)
        print(f"  expected result: ", expected)
        print(f"  submitted result:", result)
        score_sum = 0
        assert list(self.scores.keys()) == list(expected.keys())
        assert list(self.scores.keys()) == list(result.keys())

        for test_key in self.scores:
            if expected[test_key] == result[test_key]:
                score_sum += self.scores[test_key]
                print(f"  {self.target_name}/{test_key} scored {self.scores[test_key]}")
            else:
                print(f">>{self.target_name}/{test_key} FAILED")
        print(f"{self.target_name} scored {score_sum}")
        return score_sum


class EvalCountWords(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "count_words"
        self.scores = {"basic": 4, "applied": 4}

    def run(self, module):
        text = "for the people by the people of the people"
        basic_res = self.try_run(module.count_words, text)
        text = "나는 너를 좋아하고 너를 좋아하고 너도 나를 좋아하고 나를 좋아하고 " \
               "우린 서로 좋아하는데도 그 누구도 말을 안 해요"
        applied_res = self.try_run(module.count_words, text)
        return {"basic": basic_res, "applied": applied_res}


class EvalAverageListSimple(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "average_list_simple"
        self.scores = {"basic": 4, "applied": 4}
        self.data = np.random.rand(8).round(3).tolist()
        print("data to average:", self.data)

    def run(self, module):
        data = [1, 2, 3, 4, 5]
        basic_res = self.try_run(module.average_list_simple, data)
        applied_res = self.try_run(module.average_list_simple, self.data)
        return {"basic": basic_res, "applied": applied_res}


class EvalAverageListComplex(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "average_list_complex"
        self.scores = {"basic": 4, "startend": 4, "skipval": 4}
        self.data = np.random.rand(8).round(3).tolist()
        print("data to average:", self.data)

    def run(self, module):
        data = [1, 2, 3, 4, 5]
        basic_res = self.try_run(module.average_list_complex, data)
        startend_res = self.try_run(module.average_list_complex, self.data, 1, 6)
        skipval_res = self.try_run(module.average_list_complex, data, skip_values=[2, 4])
        return {"basic": basic_res, "startend": startend_res, "skipval": skipval_res}


class EvalAddLists(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "add_lists"
        self.scores = {"basic": 4, "applied": 4}
        self.data1 = np.random.rand(8).round(3).tolist()
        self.data2 = np.random.rand(8).round(3).tolist()
        print("data to add lists:", self.data1, self.data2)

    def run(self, module):
        foo = [1, 2, 3, 4, 5]
        bar = [1, 2, 3, 4, 5]
        basic_res = self.try_run(module.add_two_lists, foo, bar)
        applied_res = self.try_run(module.add_two_lists, self.data1, self.data2)
        return {"basic": basic_res, "applied": applied_res}


class EvalAddDicts(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "add_dicts"
        self.scores = {"basic": 6, "applied": 6}
        self.data1 = dict(zip(["foo", "bar", "goo", "qux", 1, 2, 3, 4], np.random.rand(8).round(3).tolist()))
        self.data2 = dict(zip(["foo", "bar", "goo", "qux", 1, 2, 3, 4], np.random.rand(8).round(3).tolist()))
        print("data to add dicts:", self.data1, self.data2)

    def run(self, module):
        foo = {1: 1, 2: 2, 3: 3, 4: 4}
        bar = {3: 1, 1: 3, 2: 2, 5: 5}
        basic_res = self.try_run(module.add_two_dicts, foo, bar)
        applied_res = self.try_run(module.add_two_dicts, self.data1, self.data2)
        return {"basic": basic_res, "applied": applied_res}


class EvalReplaceWord(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "replace_word"
        self.scores = {"basic": 5, "applied": 5}

    def run(self, module):
        text = "or the people by the people of the people"
        srcfile = "__test__/sample.txt"
        dstfile = "__test__/sample_revised.txt"
        with open(srcfile, "w") as f:
            f.write(text)
        self.try_run(module.replace_word_in_file, srcfile, "people", "python", dstfile)
        with open(dstfile, "r") as f:
            basic_res = f.read()

        text = "산토끼 토끼야 어디를 가느냐?"
        with open(srcfile, "w") as f:
            f.write(text)
        self.try_run(module.replace_word_in_file, srcfile, "토끼", "딸기", dstfile)
        with open(dstfile, "r") as f:
            applied_res = f.read()

        return {"basic": basic_res, "applied": applied_res}


class EvalFileManager(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "file_manager"
        self.scores = {"init_items": 4, "init_files": 4, "init_dirs": 4,
                       "make_dir": 4, "remove_dir": 4, "remove_file": 4}

    def run(self, module):
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

        init_items, init_files, init_dirs, make_dir, remove_dir, remove_file = None, None, None, None, None, None
        try:
            filemng = module.FileManager(rootpath)
            init_items = filemng.items
            init_files = filemng.get_files()
            init_dirs = filemng.get_dirs()

            filemng.make_dir("melon")
            file_correct = midcor.FileManager(rootpath)
            make_dir = file_correct.get_dirs()
            filemng.remove_dir("apple")
            file_correct = midcor.FileManager(rootpath)
            remove_dir = file_correct.get_dirs()
            filemng.remove_file("cherry.txt")
            file_correct = midcor.FileManager(rootpath)
            remove_file = file_correct.get_files()
        except Exception as e:
            print("Exception:", e)

        return {"init_items": init_items, "init_files": init_files, "init_dirs": init_dirs,
                "make_dir": make_dir, "remove_dir": remove_dir, "remove_file": remove_file}


class EvalSum2D(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "sum_array2d"
        self.scores = {"d1col1": 2, "d1col5": 2, "d2col2": 2, "d2col8": 2}
        self.data = np.random.rand(4, 3).round(3)
        print("data to sum:", self.data)

    def run(self, module):
        data = [list(range(i * 3, (i + 1) * 3)) for i in range(3)]
        data = np.array(data)
        print("[EvalSum2D] data:", data)
        d1col1 = module.sum_array2d_column(data, 1)
        d1col5 = module.sum_array2d_column(data, 5)
        d2col2 = module.sum_array2d_column(self.data, 2)
        d2col8 = module.sum_array2d_column(self.data, 8)
        return {"d1col1": d1col1, "d1col5": d1col5, "d2col2": d2col2, "d2col8": d2col8}


class EvalCorrelation(EvalTemplate):
    def __init__(self):
        super().__init__()
        self.target_name = "sum_array2d"
        self.scores = {"cpp_high": 2, "cpp_low": 2, "cs_high": 3, "cs_low": 3}
        self.java = np.random.rand(4, 3).round(3)
        self.csharp = np.random.rand(4, 3).round(3)
        print("correlation data:", self.java, self.csharp)

    def run(self, module):
        python = np.array([[1, 2, 3], [7, 8, 9], [4, 5, 6]])
        cpp = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
        cpp_high_python_mean, cpp_low_python_mean = self.try_run(module.score_correlation, python, cpp)
        cs_high_java_mean, cs_low_java_mean = self.try_run(module.score_correlation, self.java, self.csharp)
        return {"cpp_high": cpp_high_python_mean, "cpp_low": cpp_low_python_mean,
                "cs_high": cs_high_java_mean, "cs_low": cs_low_java_mean}


if __name__ == "__main__":
    total_score = 0
    total_score += EvalCountWords().evaluate()
    total_score += EvalAverageListSimple().evaluate()
    total_score += EvalAverageListComplex().evaluate()
    total_score += EvalAddLists().evaluate()
    total_score += EvalAddDicts().evaluate()
    total_score += EvalReplaceWord().evaluate()
    total_score += EvalFileManager().evaluate()
    total_score += EvalSum2D().evaluate()
    total_score += EvalCorrelation().evaluate()
    print("="*30)
    print("Total score:", total_score)









