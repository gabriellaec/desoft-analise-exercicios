with open('churras.txt','r') as texto:
    conteudo = texto.read
conteudo.split(',')
print (n)
del n[0,:,3]
valor = 0
i = 0
while i <= len(n):
    valor += n[i]*n[i+1]
    i += 2
print(valor)