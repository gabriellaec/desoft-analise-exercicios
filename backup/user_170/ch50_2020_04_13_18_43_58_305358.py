def junta_nome_sobrenome(nomes, sobrenomes):
    juntos = []
    i =0
    while i < len(nomes):
        juntos.append(nomes[i]+(' {}'.format(sobrenomes[i])))
        i +=1
    return juntos