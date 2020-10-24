def junta_nome_sobrenome(a, b):
  lista =[]
  i = 0
  while i < len(a):
    lista.append(a[i] + " " + b[i])
    i += 1
  return lista
c = []
d = []
print(junta_nome_sobrenome(c,d))
    