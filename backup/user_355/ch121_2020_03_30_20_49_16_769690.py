lista1=[0,2,4,6,8,10,12,14,16,18,20]
lista2=[0,3,6,9,12,15,18,21]
lista1_menos_lista2=[]
a=0
def encontar(x,lista):
  y=len(lista)
  x=lista1[0]
  while a < y:
    if x!=lista[a]:
      lista1_menos_lista2.append(x)
    else:
      return False
    a+=1
    
'''def subtracao_de_listas:
    while lista1[0]!=lista2[0]
    a+=1
    lista1_menos_lista2.append([0])
print(subtracao_de_lista)'''