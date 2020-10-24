def junta_nome_sobrenome(nomes,sobrenomes):
    i=0
    while i<len(nomes) and i<len(sobrenomes):
        print('{0} {1}'.format(nomes[i],sobrenomes[i]))
        i+=1
        return i
        