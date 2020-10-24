with open('churras.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        
custo = 0
i=1
while i<len(palavras) - 1:
    custo += int(palavras[i])*float(palavras[i+1])
    i+=3

print(custo)
