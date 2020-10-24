def intersecccao_valores (m,n):
    lista = []
    for k,v in m.itens():
        for k1,v1 in n.itens():
            if k == k1:
                lista.append(k)
                return lista
                
            