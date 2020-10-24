lista=[]
palavra="salame"
while palavra != "fim":
    palavra=input("digite uma palavra: ")
    lista.append(palavra)
    
i=0
while i<=len(lista):
    if lista[i[0]]!="a":
        lista.remove(lista[i])
    i+=1
z=0    
while z!=len(lista):
    print (lista[z])
    z+=1