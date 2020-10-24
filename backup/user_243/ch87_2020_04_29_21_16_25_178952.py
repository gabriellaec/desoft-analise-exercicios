with open ("churras.txt",'r') as arquivo:
    conteudo=arquivo.readlines()
    x=0
    for i in conteudo:
        i=linha.split()
        x=x+(float(lista[1])*(lista[2]))
print(x)    