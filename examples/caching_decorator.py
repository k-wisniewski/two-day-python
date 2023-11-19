from functools import wraps
from time import sleep


def cache(max_size=10):
    def decorator(f):
        _cache = {}

        def _ensure_space_left_in_cache():
            if len(_cache) == max_size:
                _cache.pop(next(iter(_cache)))
        
        @wraps(f)
        def wrapper(*args, **kwargs):
            cache_key = f"{f.__name__}_{'_'.join(map(str, args))}_{'_'.join(f'{k}={v}' for k, v in kwargs.items())}"

            if cache_key not in _cache:
                _ensure_space_left_in_cache()
                _cache[cache_key] = f(*args, **kwargs)
            return _cache[cache_key]
        return wrapper
    return decorator

@cache(max_size=2)
def slow_adder(x, y):
    sleep(5)
    return x + y

@cache()
def slow_multiplier(x, y):
    sleep(5)
    return x * y

print(slow_adder(2,5))
print(slow_adder(3,5))
print(slow_adder(2,5))
print(slow_adder(2,5))
print(slow_adder(2,5))
print(slow_adder(2,5))
print(slow_adder(2,5))
print(slow_adder(2,5))
print(slow_adder(2,5))
print(slow_multiplier(2,5))
print(slow_multiplier(2,5))
print(slow_multiplier(2,5))
print(slow_multiplier(2,5))
print(slow_adder(2,5))
print(slow_adder(3,5))
print(slow_adder(4,5))
print(slow_adder(5,5))
print(slow_adder(4,5))

