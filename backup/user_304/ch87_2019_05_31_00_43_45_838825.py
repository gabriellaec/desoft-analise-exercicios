with open('churras.txt', 'r') as arquivo:
    conteudo=arquivo.read()

lista=conteudo.splint(',')

i=1
custo=0
while i<len(lista)-1:
    preco=lista[i]*lista[i+1]
    custo+=preco
    i+=3
print(custo)
    