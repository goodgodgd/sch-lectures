# dict_ops.py
def add(foo, bar):
    # out = {}
    # for key in foo:
    #     if key in bar:
    #         out[key] = foo[key] + bar[key]
    out = {key: foo[key] + bar[key] for key in foo}
    return out


def subtract(foo, bar):
    out = {}
    for key in foo:
        if key in bar:
            out[key] = foo[key] - bar[key]
    return out


def multiply(foo, bar):
    out = {}
    for key in foo:
        if key in bar:
            out[key] = foo[key] * bar[key]
    return out


def divide(foo, bar):
    out = {}
    for key in foo:
        if key in bar:
            out[key] = foo[key] / bar[key]
    return out
