with open('churras.txt','r') as texto:
    conteudo = texto.read
    conteudo = conteudo.split(',')
del conteudo[0,:,3]
valor = 0
i = 0
while i <= len(conteudo):
    valor += conteudo[i]*conteudo[i+1]
    i += 2
print(valor)