import math

def f(s, a):
    x = s / a
    tanh_x = math.tanh(x)   #f(s) = tanh(s/a)
    return tanh_x

s = 2
a = 1.5
output = f(s, a)
print(output)  
