# functions can be treated as objects
import time


def shout(text):
    return text.upper()


# print(shout('Hello'))

yell = shout


# print(yell('hello'))

# passing function as argument

def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


# greet(shout)
# greet(whisper)

# return function from another function

def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)


# print(add_15(10))

# Defining a decorator
# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('-----------something before function')
#         res = func(*args, **kwargs)
#         print('-----------something after function')
#         return res
#
#     return wrapper
#
#
# def some_func(title, tag):
#     print(f'{title} {tag}')
#     return f'<{tag}>{title}</{tag}>'
#
#
# f = func_decorator(some_func)
# res = f('python forever', 'h1')
# print(res)

# second decorator example


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Time of working: {dt} seconds')
        return res

    return wrapper


@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

# we don't need to make another reffer to decorator function, we can use @function
# get_nod = test_time(get_nod)
# get_fast_nod = test_time(get_fast_nod)
res = get_nod(2, 1000000)
res_fast = get_fast_nod(2, 100000)
# print(res, res_fast)


# chaining decorators
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1 # first
@decor # second
def num():
    return 10
@decor # first
@decor1 # second
def num2():
    return 10

print(num()) # 400
print(num2()) # 200
