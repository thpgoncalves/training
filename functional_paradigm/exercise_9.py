# Create a function compose(f, g) that returns a new function that applies g then f. 
# That is, compose(f, g)(x) = f(g(x)). Define two pure functions, for example 
# increment(x) = x + 1 and double(x) = x * 2.
# Use compose to create new_func = compose(increment, fold) and test it, showing the result for different values of x.

from typing import Callable

def compose(f: Callable, g: Callable) -> Callable:
    """
    Returns a function that applies g(x) and then f
    i.e. compose(f, g)(x) = f(g(x)).
    """
    return lambda x: f(g(x))

def increment(n: int) -> int:
    return n + 1

def duplicate(n: int) -> int:
    return n * 2

new_func = compose(increment, duplicate)
res1 = new_func(3) 
res2 = new_func(4) 

print(res1)
print(res2)