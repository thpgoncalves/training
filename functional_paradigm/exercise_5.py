# Create a function called filter_strings_a that receives a list of strings 
# and returns only those that start with the letter 'a'. Use filter and 
# lambda (or a pure function). 
# Example: if the list is [“apple”, “pineapple”, “banana”, “plum”, “apricot”, “grape”], 
# the result should be [“apple”, “apricot”].

from typing import List 

def filter_strings(words: List[str], x: str) -> List[str]:
    filtered_list = list(filter(lambda s: s[0] == x, words))
    return filtered_list

words = ["apple", "pineapple", "banana", "plum", "apricot", "grape"]
res = filter_strings(words, 'b')
print(f"Old list: {words}")
print(f"New list: {res}")
