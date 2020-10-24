with open('texto.txt','r') as arquivo:
    conteudo = arquivo.read()
contador = 0
z = conteudo.strip()
palavra = z.split(' ')
for x in palavra:
    contador += 1
print(contador)
    
    