# Create a function called raise_squared that receives a list of integers
# and returns a new list with each value squared. Use the function and 
# lambda (or define a pure function to square).

from typing import List

def raise_squared(nums: List[int]) -> List[int]:
    """
    Returns a new list with each element squared.
    Does not modify the original list.
    """
    new_list = list(map(lambda x: x ** 2, nums))
    return new_list

nums = [1, 2, 3, 4, 5, 6, 7, 8]
res = raise_squared(nums)
print(f"Old list: {nums}")
print(f"New list: {res}")