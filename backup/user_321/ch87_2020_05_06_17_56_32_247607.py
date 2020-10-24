with open('churras.txt','r') as texto:
    conteudo = texto.read()
n = conteudo.split('n')
valor = 0
i = 0
while i <= len(n):
    valor += n[i]*n[i+1]
    i += 2
print(valor)