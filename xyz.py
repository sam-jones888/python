def func(x,y):
  a = 0
  b = 0
  z = a + b
  a += x
  b += y
  if z == 0:
    z ** 2
  return z
x = int(input())
y = int(input())
func(x,y)
print(x,y)
