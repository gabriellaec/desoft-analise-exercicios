with open('churras.txt','r') as texto:
    conteudo = texto.read()
valor = 0
n = conteudo.split('\n')
e = n.split(',')
print(e)
for i in conteudo: 
    valor += int(e[1])*float(e[2])
print(valor)