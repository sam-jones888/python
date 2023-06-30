import math

def fermi(s, a):
    return 1 / (1 + math.exp(-2 * a * s))        #f(s) = 1 / (1 + e^(-2as))

result = fermi(1.5, 0.8)
print(result)
