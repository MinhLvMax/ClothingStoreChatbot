import logging
from functools import wraps
import time


def short_repr(obj, max_length=10):
    r = repr(obj)
    return r if len(r) <= max_length else r[:max_length] + '...'


logging.basicConfig(level=logging.INFO,
                    format=f"%(asctime)s - %(levelname)s - %(message)-50s")


def record_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [short_repr(a) for a in args]
        kwargs_repr = [f"{k}={short_repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        try:
            logging.info(f"Executing {func.__name__}({signature}).")
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed = (end - start)
            logging.info(f"Executed  {func.__name__}({signature}) in {elapsed:.2f}s.")
            return result
        except Exception as e:
            logging.error(f"Have an eror!")
            raise e

    return wrapper
