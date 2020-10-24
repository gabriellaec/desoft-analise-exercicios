terminar = True
lista=[]
ultimo = 0
while terminar :
    a = input("me diga uma palavra:  ")
    

    if(a == 'fim' ):
        terminar = False
  
    else :
        lista.append(a)


while(ultimo < len(lista)):
    palavra = lista[ultimo]
    if(palavra[0] != 'a' ):
        del lista[ultimo]
    ultimo+=1

print(lista)