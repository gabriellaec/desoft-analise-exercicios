with open('churras.txt','r') as texto:
    conteudo = texto.read()
n = conteudo.split(',')
valor = 0
i = 0
while i <= len(n):
    valor += int(n[i])*int(n[i+1])
    i += 2
print(valor)