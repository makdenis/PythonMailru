import json


def to_json(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, dict):
            print("dictionary")
            print(json.dumps(res))
        else:
            print("not a dictionary")
            print(res)
        return res

    return inner


@to_json
def func():
    return {1: 1,  2: 2, 3: 3}


@to_json
def func2(str):
    return str


a = "string"
func()
func2(a)
