# Create a pure function called sum that receives two numbers and returns
# their sum. Show how to call it and print the result.

def sum(a,b):
    """
    Pure function that sums two values.
    - Always returns the same result for the same parameters.
    - No side effects.
    """
    return a + b

res = sum(2,3)
print(res)