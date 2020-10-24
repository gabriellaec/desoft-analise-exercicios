palavra=str(input("Escreva uma palavra"))
lista1=[]            
while palavra != 'fim':
    lista1.append(palavra)
    palavra=str(input("Escreva uma palavra"))

i=0              
while i < len(lista1):
    if lista1[i][0] == "a":
        print(lista1[i])
        i+=1              
    else:
        i+=1              