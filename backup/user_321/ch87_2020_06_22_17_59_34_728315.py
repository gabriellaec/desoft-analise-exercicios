with open('churras.txt','r') as texto:
    conteudo = texto.read()
valor = 0
n = conteudo.strip()
e = n.split(',')
e = e.split('\n')
print(e)
for i in conteudo:
   
    
    valor += int(e[1])*float(e[2])
print(valor)