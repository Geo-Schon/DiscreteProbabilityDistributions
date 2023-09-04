from math import factorial, exp


def puasson(m, p, n):
    λ = p * n
    return exp(-λ) * (λ ** m) / factorial(m)


def bernulli(n, k, p):
    formula = factorial(n)/(factorial(k)*factorial(n-k))
    return formula*(p**k)*(1-p)**(n-k)


def combination(i, j):
    return (factorial(i) / (factorial(j) * factorial(i-j)))