with open('churras.txt','r') as texto:
    conteudo = texto.read()
valor = 0
for i in conteudo:
    n = conteudo.strip()
    e = i.split(',')
    print(e)
    
    valor += int(e[1])*float(e[2])
print(valor)