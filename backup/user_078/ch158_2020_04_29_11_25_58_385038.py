with open ('texto.txt', 'r') as arquivo:
    conteudo = arquivo.split()

contador = 0
for palavra in conteudo:
    contador += 1
    
    