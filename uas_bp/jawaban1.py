def factor(n):
    if n == 1:
        return n
    else:
        return n + factor(n-1)

print(factor(4))

#rekursif while
def factorial(n):
    hasil = 1
    while n > 0:
        hasil = hasil * n
        n = n - 1
    return hasil

print(factorial(4))

#fibonanci
def fibonanci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonanci(n-2) + fibonanci(n-1)

print(fibonanci(5))


