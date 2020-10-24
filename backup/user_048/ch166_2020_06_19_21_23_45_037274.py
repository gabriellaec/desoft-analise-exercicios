def total_do_semestre_por_bairro(dicio_inic):
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

    dicio=dict(zip(lista_bairros, lista_novos_valores))
    return dicio