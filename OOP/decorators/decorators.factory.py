"""
This code shows how to write a decorator factory.
If you recall, decorating a function with a decorator that takes
arguments is the same as writing func = decorator(arg A, argB) (func)
so when we decorate cube with max_result(75), we're decorating
cube = max_result(75)(cube)
"""
from functools import wraps

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(
                'Result is too big ({0}). Max allowed is {1}.'
                .format(result, threshold)
                )
                return result
            return wrapper
        return decorator

  @max_result(75)
  def cube(n):
      return n ** 3

  @max_result(100)
  def square(n):
      return n ** 2

  @max_result(1000)
  def multiply(a, b):
      return a * b
