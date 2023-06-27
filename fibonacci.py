a, b = 0, 1
while True:
  a, b = b, a + b
  if a == 34:
    break
  print(a)
