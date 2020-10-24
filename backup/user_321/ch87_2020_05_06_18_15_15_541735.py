with open('churras.txt','r') as texto:
    conteudo = texto.read()
n = conteudo.split(',')
i=0
while i < len(n):
    del n[i]
    i +=2
valor = 0
i = 0
while i <= len(n):
    valor += int(n[i])*int(n[i+1])
    i += 1
print(valor)