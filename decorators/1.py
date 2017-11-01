import time


def log_duration(func):
    def inner(*args, **kwargs):
        timer = time.clock()
        res = func(*args, **kwargs)
        print("duration : " + str(time.clock() - timer))
        return res

    return inner


@log_duration
def print_l(lst):
    for i in lst:
        print(str(i))


a = [1, 2, 3, 4, 5]
print_l(a)
