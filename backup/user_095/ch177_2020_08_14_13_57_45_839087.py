def numero_digitos(s):
  soma = 0
  for e in s:
    if e.isdigit():
      soma+=1
  return soma