import sys
import os
import shutil
import numpy as np

import midterm as sub
import midterm_correct_answer as cor


filemng_sub = None
filemng_cor = None


def eval_template(test, target_name, score):
    try:
        result, expected = test()
        assert result == expected, f"Wrong result: {result} != {expected}"
        print(f"  ({target_name}/{test.__name__}) scored {score}")
        return score
    except Exception as e:
        print(f"  ({target_name}/{test.__name__}) failed: ({type(e)})", e)
        return 0


class EvalFormat(object):
    def __init__(self, target_name):
        self.target_name = target_name
        self.score = 0

    def __enter__(self):
        print(f"[{self.target_name}] ----------")
        return self

    def __exit__(self, type, value, trace_back):
        print(f"[{self.target_name}] score:", self.score)


def eval_count_words(target_name):
    def basic():
        text = "for the people by the people of the people"
        return sub.count_words(text), cor.count_words(text)

    def advanced():
        text = "나는 너를 좋아하고 너를 좋아하고 너도 나를 좋아하고 나를 좋아하고 " \
               "우린 서로 좋아하는데도 그 누구도 말을 안 해요"
        return sub.count_words(text), cor.count_words(text)

    score = 0
    score += eval_template(basic, target_name, 4)
    score += eval_template(advanced, target_name, 4)
    return score


def eval_file_manager(target_name):
    global filemng_sub, filemng_cor
    rootpath_sub = "./test_sub"
    rootpath_cor = "./test_cor"
    directories = ["apple", "banana"]
    files = ["cherry.txt", "mango.txt"]

    def prepare(root, dirnames, filenames):
        if os.path.isdir(root):
            shutil.rmtree(root)
        os.mkdir(root)
        for dname in dirnames:
            os.mkdir(os.path.join(root, dname))
        for fname in filenames:
            with open(os.path.join(root, fname), "w") as f:
                f.write(fname)

    prepare(rootpath_sub, directories, files)
    prepare(rootpath_cor, directories, files)

    def basic_init():
        global filemng_sub, filemng_cor
        filemng_sub = sub.FileManager(rootpath_sub)
        filemng_cor = sub.FileManager(rootpath_cor)
        results_cor = [item.replace(rootpath_cor, rootpath_sub) for item in filemng_cor.items]
        return filemng_sub.items, results_cor

    def basic_get_files():
        global filemng_sub, filemng_cor
        results_cor = filemng_cor.get_files()
        results_cor = [item.replace(rootpath_cor, rootpath_sub) for item in results_cor]
        return filemng_sub.get_files(), results_cor

    def basic_get_dirs():
        global filemng_sub, filemng_cor
        results_cor = filemng_cor.get_dirs()
        results_cor = [item.replace(rootpath_cor, rootpath_sub) for item in results_cor]
        return filemng_sub.get_dirs(), results_cor

    def basic_make_dir():
        global filemng_sub, filemng_cor
        filemng_sub.make_dir("melon")
        filemng_cor.make_dir("melon")
        assert os.path.isdir(os.path.join(filemng_sub.rootpath, "melon")), "submitted FileManager could NOT make dir"
        assert os.path.isdir(os.path.join(filemng_cor.rootpath, "melon")), "correct FileManager could NOT make dir"
        results_cor = [item.replace(rootpath_cor, rootpath_sub) for item in filemng_cor.items]
        return filemng_sub.items, results_cor

    score = 0
    score += eval_template(basic_init, target_name, 4)
    score += eval_template(basic_get_files, target_name, 4)
    score += eval_template(basic_get_dirs, target_name, 4)
    score += eval_template(basic_make_dir, target_name, 4)
    """
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
    """
    return score


if __name__ == "__main__":
    with EvalFormat("count_words") as f:
        f.score = eval_count_words(f.target_name)
    with EvalFormat("FileManager") as f:
        f.score = eval_file_manager(f.target_name)



