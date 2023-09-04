from math import factorial as fl, exp


def puasson(m, p, n):
    λ = p * n
    return exp(-λ) * (λ ** m) / fl(m)


def bernulli(n, k, p):
    formula = fl(n)/(fl(k)*fl(n-k))
    return formula*(p**k)*(1-p)**(n-k)


def combination(i, j):
    return (fl(i) / (fl(j) * fl(i-j)))