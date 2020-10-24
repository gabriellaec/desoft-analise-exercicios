with open('churras.txt','r') as texto:
    conteudo = texto.read()
n = conteudo.split('\n')
valor = 0
i = 0
for i in n:
    for e in i:
        o = e.split(',')
        valor += int(o[1])*float(o[2])
print(valor)