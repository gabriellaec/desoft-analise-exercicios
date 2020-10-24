def login_disponivel(nome, lista):
    i=0
    if nome not in lista:
        return nome
    else:
        for item in range(len(lista)):
            while nome in lista:
                lista[item]= lista[item]+i
                i+=1
        return nome