


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


class ExecIndexWord(ExecTemplate):
    def __init__(self, module):
        super().__init__(module)
        self.target_name = "index_word"
        self.scores = {"basic": 4, "applied": 4}

    def run(self):
        self.results = {}
        text = "pick me pick me pick me up"
        f = (lambda: self.module.index_word(text, "pick"))
        self.try_run(f, "basic")
        text = "나는 너를 좋아하고 너를 좋아하고 너도 나를 좋아하고 나를 좋아하고 " \
               "우린 서로 좋아하는데도 그 누구도 말을 안 해요"
        f = (lambda: self.module.index_word(text, "좋아하"))
        self.try_run(f, "applied")
        return self.results
