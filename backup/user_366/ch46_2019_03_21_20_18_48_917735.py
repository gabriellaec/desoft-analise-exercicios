palavras = []
perg = input("Digite uma palavra: ")

while perg != 'fim':
    palavras.append(perg) 
    perg = input("Digite outra palavra: ")

i = 0 
while i <= len(palavras):
    if palavras[i][0] == 'a':
        print(palavras[i])
    else:
        del palavras[i]
    i += 1