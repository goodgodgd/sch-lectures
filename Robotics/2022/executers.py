


class ExecTemplate:
    def __init__(self, module):
        self.module = module
        self.target_name = ""
        self.scores = {}
        self.results = {}

    def run(self):
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


class Exec1IndexWord(ExecTemplate):
    def __init__(self, module):
        super().__init__(module)
        self.target_name = "index_word"
        self.scores = {"basic": 5, "applied": 5}

    def run(self):
        text = "pick me pick me pick me up"
        f = (lambda: self.module.index_word(text, "pick"))
        self.try_run(f, "basic")
        text = "나는 너를 좋아하고 너를 좋아하고 너도 나를 좋아하고 나를 좋아하고 " \
               "우린 서로 좋아하는데도 그 누구도 말을 안 해요"
        f = (lambda: self.module.index_word(text, "좋아하"))
        self.try_run(f, "applied")
        return self.results


class Exec2SumList(ExecTemplate):
    def __init__(self, module):
        super().__init__(module)
        self.target_name = "sum_list"
        self.scores = {"basic": 4, "test1": 3, "test2": 3}

    def run(self):
        data = [1, 2, 3, 100, 4, 5]
        f = (lambda: self.module.sum_list(data))
        self.try_run(f, "basic")
        f = (lambda: self.module.sum_list(data, 10))
        self.try_run(f, "test1")
        data = [4, 65, 2, 7, 9, 34, 23, 8, 56]
        f = (lambda: self.module.sum_list(data, 10))
        self.try_run(f, "test2")
        return self.results


class Exec3AddDcits(ExecTemplate):
    def __init__(self, module):
        super().__init__(module)
        self.target_name = "add_dicts"
        self.scores = {"basic": 4, "test1": 3, "test2": 3}

    def run(self):
        foo = {'kim': 1, 'lee': 2}
        bar = {'lee': 3, 'park': 4}
        f = (lambda: self.module.add_dicts(foo, bar))
        self.try_run(f, "basic")
        f = (lambda: self.module.add_dicts(foo, bar, True))
        self.try_run(f, "test1")
        foo = {'kim': 1, 'lee': 2, 'choi': 3}
        bar = {'lee': 3, 'park': 4, 'yoon': 5}
        f = (lambda: self.module.add_dicts(foo, bar, True))
        self.try_run(f, "test2")
        return self.results


class Exec4ManiList(ExecTemplate):
    def __init__(self, module):
        super().__init__(module)
        self.target_name = "mani_list"
        self.scores = {"sortfirst": 2, "pop": 2, "remove": 2, "append": 2, "sort_last": 3, "applied": 4}

    def run(self):
        tottenham = ["Son", "Kane", "Ali", "Eriksen", "Llorente"]
        f = (lambda: self.module.manipulate_list(tottenham, sort_first=True))
        self.try_run(f, "sortfirst")
        tottenham = ["Son", "Kane", "Ali", "Eriksen", "Llorente"]
        f = (lambda: self.module.manipulate_list(tottenham, pop=[1, 3]))
        self.try_run(f, "pop")
        tottenham = ["Son", "Kane", "Ali", "Eriksen", "Llorente"]
        f = (lambda: self.module.manipulate_list(tottenham, remove=["Ali", "Llorente"]))
        self.try_run(f, "remove")
        tottenham = ["Son", "Kane", "Ali", "Eriksen", "Llorente"]
        f = (lambda: self.module.manipulate_list(tottenham, append=["Kulusevski", "Richarlison"]))
        self.try_run(f, "append")
        tottenham = ["Son", "Kane", "Ali", "Eriksen", "Llorente"]
        f = (lambda: self.module.manipulate_list(tottenham, append=["Kulusevski", "Richarlison"], sort_last=True))
        self.try_run(f, "sort_last")
        tottenham = ["Son", "Kane", "Ali", "Eriksen", "Llorente"]
        f = (lambda: self.module.manipulate_list(tottenham, pop=[1, 2], remove=["Ali"],
                                                 append=["Kulusevski", "Richarlison"], sort_last=True))
        self.try_run(f, "applied")
        return self.results


class Exec5Stats(ExecTemplate):
    def __init__(self, module):
        super().__init__(module)
        self.target_name = "statistics"
        self.scores = {"mean1": 2, "max1": 2, "maxwt1": 2, "mean2": 3, "max2": 3, "maxwt2": 3}

    def run(self):
        f = (lambda: self.module.Statistics([1, 2, 3, 4, 5]).mean())
        self.try_run(f, "mean1")
        f = (lambda: self.module.Statistics([1, 2, 3, 4, 5]).max())
        self.try_run(f, "max1")
        f = (lambda: self.module.Statistics([1, 2, 3, 4, 5]).max_with([5, 4, 3, 2, 1]))
        self.try_run(f, "maxwt1")

        f = (lambda: self.module.Statistics([3.4, 2.9, 9.1, 4.6, 8.4]).mean())
        self.try_run(f, "mean2")
        f = (lambda: self.module.Statistics([3.4, 2.9, 9.1, 4.6, 8.4]).max())
        self.try_run(f, "max2")
        f = (lambda: self.module.Statistics([3.4, 2.9, 9.1, 4.6, 8.4]).max_with([7.3, 2.4, 8.5, 7.7, 3.8]))
        self.try_run(f, "maxwt2")
        return self.results


