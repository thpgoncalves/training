# Implement a function called calculate_potency(base, exponent) that returns base ** exponent.
# Create, using functools.partial, a new function to always square (exponent=2) and test it.
# Do the same for always cubing (exponent=3).

from functools import partial

def calculate_potency(base: int, expoent: int) -> int:
    return base ** expoent

# Partial function for squaring (setting exponent=2)
expo_2 = partial(calculate_potency, expoent = 2)
res1 = expo_2(3)

# Partial function for cubing (setting exponent=3)
expo_3 = partial(calculate_potency, expoent = 3)
res2 = expo_3(3)

print(res1)
print(res2)