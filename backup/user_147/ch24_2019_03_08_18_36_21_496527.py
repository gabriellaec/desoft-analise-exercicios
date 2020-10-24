def classifica_triangulo(a, b, c):
  if a == b and a == c:
    return "equilátero"
  elif a == b or b == c or a == c:
    return "isósceles"
  else:
    return "escaleno"