def login_disponivel(lg, lt):
    c = 1
    a = lg
    vai = True
    if lg not in lt:
        return lg
    while vai:
        for i in lt:

            if lg not in lt:
                vai = False
                return lg


            if i == lg:
                lg = a
                lg = lg + '{0}'.format(c)
                c +=1
                
            
    return lg

lista = []
vai = True

while vai:
    a = input("nome")
    if a == "fim":
        vai = False
    else:
        lista.append(a)

tam = len(lista)

for i in range(tam):

    sel = lista[0]
    lista.remove(sel)

    log = login_disponivel(sel, lista)

    lista.append(sel)

    print(log)

        