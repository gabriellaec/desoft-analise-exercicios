with open('churras.txt', 'r') as arquivo:
    conteudo=arquivo.read()
conteudo = conteudo.replace('\n',',')
lista = conteudo.split(',')

i=1
custo=0
while i<len(lista):
    preco=int(lista[i])*float(lista[i+1])
    custo+=preco
    i+=3
print(custo)
    