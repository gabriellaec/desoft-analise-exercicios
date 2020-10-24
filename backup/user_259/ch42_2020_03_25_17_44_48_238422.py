palavras = []
run = True
while run:
    p = input("Palavra: ")
    if p=='fim':
        run = False
    else:
        palavras.append(p)
i = 0
while i<(len(palavras)):
    primeira_letra = (palavras[i])[0]
    if primeira_letra == 'a':
        print(palavras[i])
        i+=1
    else:
        i+=1   
    
    