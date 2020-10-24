with open('churras.txt','r') as texto:
    conteudo = texto.readlines()
valor = 0
for i in conteudo: 
    n = conteudo[i].strip()
    e = n.split(',')
    print(e)
    valor += int(e[1])*float(e[2])
print(valor)