from math import factorial
def factorial2(n):
    if n < 0:
        return
    if n == 0 or n == 1:
        return 1
    f = (factorial2(n - 1) * n)
    print(f)
    return(f)

print(factorial2(5) == factorial(5))