def junta_nomes (lis1,lis2,lis3):
  ret = []
  for e in lis1:
    for i in lis3:
      ret.append(e+' '+i)
  for e in lis2:
    for i in lis3:
      ret.append(e+' '+i)
  return ret