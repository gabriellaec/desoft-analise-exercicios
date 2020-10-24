palavras = []

p = str(input('Digite uma palavra: '))
while p != 'fim':
    p = str(input('Digite uma palavra: '))
    if p[0] == 'a':
        palavras.append(p)

i = 0
while i<len(palavras):
    print(palavras[i])
    i += 1
