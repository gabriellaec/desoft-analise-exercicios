def junta_nome_sobrenome():
    nomes=['nivea','joao','alberto']
    sobrenomes=['dantas','silva','lima']
    nomes_completos=[]
    i=0
    while i != int(len(nomes)):
    nome_completo=nomes[i]+ ' ' + sobrenomes[i]
    nomes_completos.append(nome_completo)
    i=i+1
    return print(nomes_completos)
    