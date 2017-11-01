def ignore_exceptions(ex):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except ex:
                return None

            return res

        return inner

    return wrapper


@ignore_exceptions(TypeError)
def div(first, second):
    return first / second


div(1, 0)
div(1, "a")
