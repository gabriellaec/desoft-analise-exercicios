def imprime_grade(n):
  n_linhas = 2*n +1
  for e in range(n_linhas):
    if e%2==0:
      for k in range(n_linhas):
        if k%2==0:
          print("+", end='' )
        else:
          print("-", end='' )
      print ()
    else:
      for k in range(n_linhas):
        if k%2==0:
          print("|", end='' )
        else:
          print(" ", end='' )
      print()