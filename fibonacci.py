a, b = 0, 1
while True:
  a, b = b, a + b   #a, b = b, a + b
  if a == 34:       #0, 1 = 1, 0 + 1
    break
  print(b)
