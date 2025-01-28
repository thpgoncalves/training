# Create a function called concatenate_strings that uses reduce to concatenate 
# all the elements of a list of strings into a single string. For example, if 
# the list is [“I”, “love”, “Python”], the result should be “I love Python”.

from typing import List
from functools import reduce

def concatenate_strings(words: List[str]) -> str:
    phrase = reduce(lambda acc, s: acc + " " + s, words) if words else ""
    return phrase

words = ["I", "love", "Python"]
res = concatenate_strings(words)
print(f"Old list: {words}")
print(f"New list: {res}")