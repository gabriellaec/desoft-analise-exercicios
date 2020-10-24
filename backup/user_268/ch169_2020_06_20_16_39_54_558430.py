def login_disponivel(lg, lt):
    c = 1
    a = lg
    if lg not in lt:
        return lg
    for i in lt:
        
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

for i in lista:
    log = login_disponivel(i, lista)
    print(log)
    
        