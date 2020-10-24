def junta_listas(lista):
    lista1=[]
    i=0
    while i< len(lista):
        print(lista[i])
        lista1.append(str(lista[i]).strip('[]'))
        i+=1
        a=', '.join(lista1)
        b=[a]
      
    print (b)
  

  