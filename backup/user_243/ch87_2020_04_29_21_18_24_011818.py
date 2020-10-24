with open ("churras.txt",'r') as arquivo:
    conteudo=arquivo.readlines()
    x=0
    for i in conteudo:
        lista=i.split(',')
        x=x+(float(lista[1])*(float(lista[2]))
print(x)    