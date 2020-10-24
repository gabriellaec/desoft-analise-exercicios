with open ('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
lista_palavras = conteudo.split()

contador = 0
for palavra in lista_palavras:
    contador += 1
    
    