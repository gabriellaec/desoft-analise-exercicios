def  login_disponivel(a, l1):
    lista = list()
    for i in l1:
        lista.append(i)
        

    if a not in lista: 
        lista.append(a)
        return(lista)

    if a in lista:
        
        lista.append(a+"2")   
        return(lista)