palavra=input('insira')
lista=[]
i=0
lista2=[]
while palavra!='fim':
    lista.append(palavra)
    palavra=input('insira')
while i<len(lista):
    palavra=lista[i]
    if palavra[0]=='a':
        print(palavra)
    i+=1