def junta_listas(original):
    lista=[]
    for e in original:
        for x in e:
      		  lista.append(x)
    return lista
o=[[1, 2, 3], [4, 5, 6], [7, 8], [9], [10]]
print(junta_listas(o))