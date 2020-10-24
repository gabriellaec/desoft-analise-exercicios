
def junta_nome_sobrenome(nomes,sobrenomes):
    junta=[]
    i = 0
    while i<(len(nomes)):
        junta.append('{0} {1}'.format(nomes[i], sobrenomes[i]))
        i += 1
    return junta
