palavra=input("Palavra: ")
lista=[]
while palavra != 'fim':
    lista.append(palavra)
    palavra=input("Palavra: ")
    
i=0
while i < len(lista):
    if lista[i] == 'a':
        print(lista[i])
    i+=1