def f(s, a):
    absolute_s = abs(s)
    result = s / absolute_s + a     #f(s) = s / (|s| + a)
    return result

s = 10
a = 2
output = f(s, a)
print(output) 
