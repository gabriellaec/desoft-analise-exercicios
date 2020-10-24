with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    x=conteudo.split()
    h=0
    for y in x:
        h+=1
print(h)