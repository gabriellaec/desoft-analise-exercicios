with open('churras.txt','r') as texto:
    conteudo = texto.read()
valor = 0
n = conteudo.split('\\n')
print(n)
for i in conteudo: 
    e = n.split(',')
    valor += int(e[1])*float(e[2])
print(valor)