with open('churras.txt','r') as texto:
    conteudo = texto.readlines()
valor = 0
n = conteudo.strip()
print(n)
for i in conteudo: 
    e = n.split(',')
    print(e)
    valor += int(e[1])*float(e[2])
print(valor)