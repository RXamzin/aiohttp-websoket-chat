from functools import wraps
import asyncio


def async_comand(comand):
    @wraps(comand)
    def wrapper(*args, **kwargs):
        return asyncio.run(comand(*args, **kwargs))
    return wrapper