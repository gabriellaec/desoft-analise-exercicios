def intersecccao_valores (m,n):
    lista = []
    for k,v in m.itens():
        for k2,v2 in n.itens():
            if v == v2:
                lista.append(k)
                return lista
                
            