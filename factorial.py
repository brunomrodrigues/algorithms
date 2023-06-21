def factorial_result(n):
    fact = 1
    for i  in range(2, n + 1):
        fact *= i
    return fact
    
def factorial_result_rec(n):
    if n == 1: return n
    else: return n * factorial_result_rec(n - 1)

print(factorial_result(1))
print(factorial_result_rec(5))