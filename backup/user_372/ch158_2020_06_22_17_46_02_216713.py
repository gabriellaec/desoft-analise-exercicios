with open ('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    h=0
    for palavra in palavras:
        h+=1
print(h)