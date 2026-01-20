

def multiplier(a, b, c):
  """
  Multiply each variable by each other in order then sum
  """
  mult_1 = a * b
  mult_2 = a ** c
  mult_3 = b * c

  return mult_1 + mult_2 + mult_3

print (multiplier(2, 3, 5))