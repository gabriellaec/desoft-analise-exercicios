def pergunta_numero():
    on = True
    lista = []
    while on:
        numero = int(input("digite um numero: "))
        if numero == 0:
            print(sum(lista))
            break
        else:
            lista.append(numero)
            print(lista)

pergunta_numero()