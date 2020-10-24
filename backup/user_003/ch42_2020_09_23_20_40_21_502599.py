terminar = True
lista=[]
coma=[]
ultimo = 0
while terminar :
    resposta = input("me diga uma palavra:  ")
    

    if(resposta == 'fim' ):
        terminar = False
  
    else :
        lista.append(resposta)

x = len(lista)
while(ultimo < x):
    palavra = lista[ultimo]
    if( palavra[0] == 'a' ):
        coma.append(palavra)
    ultimo +=1

v = len(coma)
z=0
while(z < v):
    print(coma[z])
    z+=1
