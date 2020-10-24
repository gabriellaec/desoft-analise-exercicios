def separa_trios(listaDeEntrada):

    listaDeSaida = []

    i = 3
    while (i <= len(listaDeEntrada)):
        listaDeSaida.append(listaDeEntrada[i-3:i])
        i += 3

    if len(listaDeEntrada) % 3 != 0:
        listaDeSaida.append(listaDeEntrada[-(len(listaDeEntrada) % 3):len(listaDeEntrada)])

    return listaDeSaida