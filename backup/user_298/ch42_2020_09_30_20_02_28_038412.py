digitando = True
todas_palavras = []
while digitando:
    palavra = input("Digite uma palavra: ")
    if palavra == 'fim':
        digitando = False
    else:
        todas_palavras.append(palavra)
palavras_com_a = []
t = 0
while t < len(todas_palavras):
    if todas_palavras[t][0] == 'a':
        palavras_com_a.append(todas_palavras[t])
    t += 1
i = 0
while i < len(palavras_com_a):
    print(palavras_com_a[i])
    i += 1
