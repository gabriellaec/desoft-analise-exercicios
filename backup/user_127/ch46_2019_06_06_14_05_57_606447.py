a = input("Digite uma palavra: ")
lista=[]
i=0
while a != "fim":
    lista.append(a)
    a = input("Digite outra palavra: ")
for b in lista:
    if b[0] == 'a':
        print(b)