def ocorrencias_letras(s):
  ret = {}
  for e in s:
    if e not in ret:
      ret[e]=1
    else:
      ret[e]+=1
  return ret