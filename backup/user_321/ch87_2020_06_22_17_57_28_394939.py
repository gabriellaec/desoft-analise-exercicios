with open('churras.txt','r') as texto:
    conteudo = texto.read()
valor = 0
for i in conteudo:
    n = conteudo.strip()
    print(n)
    
    valor += int(e[1])*float(e[2])
print(valor)