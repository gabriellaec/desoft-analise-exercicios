running = True
lista_a = []
while running:
    palavra = input('Digite uma palavra: ')
    p = str(palavra)
    if p[0] == "a":
        lista_a.append(p)
    elif p == "fim":
        running = False