palavra= input("digite uma palavra")
lista=[]
contador=0
while palavra != "fim":
    if palavra not in lista:
        lista.append(palavra)
        palavra= input("digite uma palavra")
while contador<len(lista):
    if lista[contador][0]== "a":
        print(palavra)
    
        
        