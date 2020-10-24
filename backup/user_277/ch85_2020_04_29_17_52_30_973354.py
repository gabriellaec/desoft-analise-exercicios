with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.read()
    k=conteudo.upper()
lista=k.split()
contador=0
for i in lista:
    if lista[i]=='BANANA':
        contdor+=1
print(contador)