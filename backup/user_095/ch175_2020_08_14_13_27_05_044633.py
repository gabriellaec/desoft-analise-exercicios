def imprime_tabuada(n):
  for e in range(n):
    for k in range(n):
      print (str((k+1)*(e+1))+" ", end='')
    print ()