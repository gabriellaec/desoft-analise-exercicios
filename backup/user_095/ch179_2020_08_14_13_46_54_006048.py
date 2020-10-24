def posicoes_minusculas(s):
  ret = []
  for e, i in zip(s,range(len(s))):
    if e.islower():
      ret.append(i)
  return ret