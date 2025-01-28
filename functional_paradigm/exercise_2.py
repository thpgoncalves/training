# Create a function called filter_pairs that receives a list of integers 
# and uses higher-order functions (e.g. filter) to return only even numbers. 
# Tip: use lambda to check if the number is even.

from typing import List

def filter_even(nums: List[int]) -> List[int]:
    new_list = list(filter(lambda x: x % 2 == 0, nums))
    return new_list

nums = [1, 2, 3, 4, 5, 6, 7, 8]
res = filter_even(nums)
print(f"Old list: {nums}")
print(f"New list: {res}")