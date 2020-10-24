def separa_trios(nomes):
    lista_trio = []
    i = 0
    trio = []
    for nome in nomes:
        trio.append(nome)
        if i%3 == 2:
            lista_trio.append(trio)
            trio = []
        i += 1
    if i%3 != 0:
        lista_trio.append(trio)
    return lista_trio

# nomes = ['João', 'Maria', 'Tiago', 'Pedro', 'Julia', 'Laura', 'Alice']
# print(separa_trios(nomes))