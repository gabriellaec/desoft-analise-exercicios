def inverte_dicionario(dicionario):
  dict2={}
  for k in dicionario:
    if dicionario[k] not in dict2:
      dict2[dicionario[k]]=[]
    dict2[dicionario[k]].append(k)
  return dict2