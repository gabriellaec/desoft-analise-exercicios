def bairro_mais_custoso(dicio_inic):
    lista_bairros=[]
    lista_novos_valores=[]
    #leio valores do dicionario
    for bairros,gastos in dicio_inic.items():
        #vejo os bairros e os adicionos a uma lista
        lista_bairros.append(bairros)
        #defino uma constante que vai ter o valor da soma dos gastos
        novo_valor=0
        #vejo que meses contam
        for e in gastos:
            #defino que so contam os ultimos seis meses
            if gastos.index(e)>=6:
                #somo os gastos
                novo_valor+=e
        #adiciono soma a uma lista
        lista_novos_valores.append(novo_valor)
    #crio novo dicionario
    #dicio=dict(zip(lista_bairros, lista_novos_valores))
    maior_custo=max(lista_novos_valores)
    indice=lista_novos_valores.index(maior_custo)
    bairro_mais_caro=lista_bairros[indice]
    return bairro_mais_caro