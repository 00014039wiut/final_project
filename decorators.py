# def my_decorator(func):
#     def wrapper():
#         print('first running print function before func')
#         func()
#         print('second running print function after func')
#
#     return wrapper
#
#
# @my_decorator
# def say_hello():
#     print('Hello')


# say_hello()
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Wrapper function running')
#         result = func(*args, **kwargs)
#         return result
#
#     return wrapper

#
# @decorator
# def greet(name):
#     return f'Hello {name}'
#
#
# result = greet('John')
# print(f'Result : {result}')
# def sequence(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
#
# @sequence(5)
# def greet(name):
#     print(f'Hello {name}')
#
#
# (greet('John'))

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args:{args} => kwargs : {kwargs}')
        result = func(*args, **kwargs)
        print(f'Result of {result}')
        return result

    return wrapper


@my_decorator
def add_number(*args, **kwargs):
    res = kwargs['a'] + kwargs['b']
    return res


response = add_number(3, 4, 5, a=3, b=4)
print(response)
