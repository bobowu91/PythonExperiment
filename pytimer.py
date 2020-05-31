'''
python decorator wraps your function and extend its output or funactionality.
python function itself is an object, that is why it can be called, passed in as
a function argument and returned as a fucntion output.
'''


def process_time(f, *args, **kwargs):
    def func(*args, **kwargs):
        import timeit
        start = timeit.default_timer()
        val = f(*args, **kwargs)
        print(f"runtime of {f.__name__} : {timeit.default_timer() - start}")
        return val
    return func


def memory_allocation(f, *args, **kwargs):
    pass
