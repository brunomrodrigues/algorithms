def factorial_result(n):
    fact = 1
    for i  in range(2, n + 1):
        fact *= i
    return fact
    
print(factorial_result(1))

def factorial_result_rec(n):
    if n == 1:
        return n
    else:
        temp = factorial_result(n - 1)
        temp = temp * n
    return temp
    
print(factorial_result_rec(1))