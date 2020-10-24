lista=[]
palavra="salame"
while palavra != "fim":
    palavra=input("digite uma palavra: ")
    if palavra[0]=="a":
        lista.append(palavra)
z=0    
while z!=len(lista):
    print (lista[z])
    z+=1