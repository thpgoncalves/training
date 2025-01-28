# Create a function called pipeline_numeros that receives a list of integers 
# and does the following in a pipeline (or in separate functions, which you 
# then combine):

# Filter out only the positive numbers.
# Calculate the double of each positive number.
# Add up all the resulting values.
# Tip: use filter, map and reduce functionally.

from functools import reduce
from typing import List

def pipeline_nums(nums: List[int]) -> int:
    """
    1. Filters out only the positives
    2. Fold each number
    3. Add everything up
    """
    return sum_list(double_nums(filter_positive(nums)))

def sum_list(nums: List[int]) -> int:
    """
    Add everything up from a list.
    """
    sum_result = reduce(lambda acc, x: acc + x, nums)
    return sum_result

def double_nums(nums: List[int]) -> List[int]:
    """
    Fold each number from a list.
    """
    doubled_list = list(map(lambda x: x * 2, nums))
    return doubled_list

def filter_positive(nums: List[int]) -> List[int]:
    """
    Filters out only the positives of a list in a new list.
    """
    filtered_nums = list(filter(lambda x: x if x >= 0 else "", nums))
    return filtered_nums

nums = [-5, -3, 1, 0, -10, 10, 4, 8]
res = pipeline_nums(nums)
print(f"Old list: {nums}")
print(f"New list: {res}")