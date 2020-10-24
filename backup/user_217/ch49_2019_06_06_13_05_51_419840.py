lista = []

contador = 0
ci = True

while ci :
    pergunta=int(input("Digite numeros inteiros: " ))

    if pergunta > contador:
        lista.append(pergunta)
        
    else:
        ci = False
        
print(lista)