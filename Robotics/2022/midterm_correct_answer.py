def index_word(text, word):
    result = []
    index = -1
    while 1:
        index = text.find(word, index+1)
        if index >= 0:
            result.append(index)
        else:
            break
    return result


def sum_list(data, outlier=None):
    result = 0
    for d in data:
        if outlier and d < outlier:
            result += d
        if outlier is None:
            result += d
    return result


def add_dicts(foo, bar, outer=False):
    result = {k: v for k, v in foo.items()}
    for bk, bv in bar.items():
        if bk in foo:
            result[bk] += bv
        elif outer:
            result[bk] = bv
    return result


def manipulate_list(data, sort_first=False, pop=None, remove=None, append=None, sort_last=False):
    if sort_first:
        data.sort()
    if pop:
        pop.sort()
        for pi, index in enumerate(pop):
            data.pop(index - pi)
    if remove:
        for item in remove:
            if item in data:
                data.remove(item)
    if append:
        for item in append:
            data.append(item)
    if sort_last:
        data.sort()
    return data


class Statistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def max(self):
        return max(self.data)

    def max_with(self, other):
        result = []
        for s, o in zip(self.data, other):
            result.append(max(s, o))
        return result




