lis = True
lista = []
i=0

while lis:
    palavra = str(input("Digite a palavra: "))
    if palavra == "fim":
        lis=False
    elif palavra [0] == "a":
        lista.append (palavra)
        i+=1
n=0
while n <i:
    print (lista [n])
    n+=1