def monta_mala(lista_pesos):
    lista_adicionados = []
    if sum(lista_pesos)<=23:
        return lista_pesos
    else:
        i = 0
        while i<len(lista_pesos):
            lista_adicionados.append(lista_pesos[i])
            if sum(lista_adicionados)>23:
                del lista_adicionados[i]
                return lista_adicionados
            else:
                i+=1