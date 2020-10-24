with open('churras.txt','r') as texto:
    conteudo = texto.read()
valor = 0
for i in conteudo:
    e = i.split(',')
    n = conteudo.strip()
    valor += int(e[1])*float(e[2])
print(valor)