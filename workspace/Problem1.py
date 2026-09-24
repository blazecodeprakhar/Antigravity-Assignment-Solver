def print_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return []
    a, b = 0, 1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

n_terms = 10
result = print_fibonacci(n_terms)
print(f"Fibonacci series up to {n_terms} terms:")
print(result)
