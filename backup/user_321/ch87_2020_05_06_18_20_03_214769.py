with open('churras.txt','r') as texto:
    conteudo = texto.read()
n = conteudo.split('\n')
valor = 0
i = 0
for i in n:
    e = i.split(',')
    valor += int(e[1])*float(e[2])
print(valor)