def inverte_lista(a):
  lista = []
  i = 0
  d = len(a)
  while i != len(a):
        i += 1
        lista.append(a[d-1])
        d -= 1
  return lista
n = []
print(inverte_lista(n))