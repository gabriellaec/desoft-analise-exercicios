with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.read()
    k=conteudo.upper()
lista=k.split()
contador=0
for i in range(0,len(lista)):
    if lista[i]=='BANANA':
        contador+=1
print(contador)