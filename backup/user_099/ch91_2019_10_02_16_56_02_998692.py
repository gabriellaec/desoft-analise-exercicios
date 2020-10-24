with open('palavras.txt','r') as arquivo:
    conteudo=arquivo.read()
contador=0
lista_palavras=conteudo.split()
for palavra in lista_palavras:
    if palavra[0]=='a' or palavra[0]=='A':
        contador+=1
print('Existem {0} palavras que começam com a letra "a/A" no seu texto.'.format(contador))
