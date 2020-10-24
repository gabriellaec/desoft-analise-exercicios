palavra=input('insira')
lista=[]
while palavra!='fim':
    lista.append(palavra)
    palavra=input('insira')
if palavra=='fim':
    print(lista)