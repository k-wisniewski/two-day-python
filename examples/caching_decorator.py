from time import sleep


def cache(max_size=10):
    ...

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

