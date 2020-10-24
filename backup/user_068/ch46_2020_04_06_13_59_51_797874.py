#def numero_no_indice(a):
    #lista = [1, 3, 2, 4]
    #while a < len(lista):
     #   if a != lista[a]:
      #      return False
       #     a += 1
        #else:
         #   print(lista[a])
   # return True
    
def numero_no_indice(a):
    b = []
    for i in range(len(a)):
        if i == a[i]:
            b.append(a[i])
    return b