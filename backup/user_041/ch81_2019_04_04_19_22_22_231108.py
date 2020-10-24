def interseccao_valores(dic1,dic2):
    lista=[]
    for k,v in dic1:
        if v in dic2:
            lista.append(v)
      	return lista