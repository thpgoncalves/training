# Crie uma função pura chamada fibonacci(n) que retorne o n-ésimo termo da sequência 
# de Fibonacci usando recursão. A sequência de Fibonacci é:
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2) para n > 1
# Faça de forma funcional, sem usar variáveis mutáveis, laços for ou while.

def fibonacci(n: int) -> int:
    """
    Returns the nth term of the Fibonacci sequence recursively.
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    """
    if n < 0:
        return f"The index N cant be negative."
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(6):
    print(fibonacci(n))
     