terminar = True
lista=[]
ultimo = 0
while terminar :
    resposta = input("me diga uma palavra:  ")
    

    if(resposta == 'fim' ):
        terminar = False
  
    else :
        lista.append(resposta)


while(ultimo < len(lista)):
    palavra = str(lista[ultimo])
    teste = palavra[0]
    a = 'a'
    if( teste != a ):
        break
    if( teste == a ):
        lista.remove(ultimo)
    ultimo +=1

print(lista)
