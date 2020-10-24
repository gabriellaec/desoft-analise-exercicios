def junta_nome_sobrenome (nomes,sobrenomes):
    juntalistas = []
    i = 0
    while i < len(nomes):
        juntalistas.append(str(nomes[i]) + str(sobrenomes[i]))
        i+=1
    return juntalistas 
        