def verifica_lista(l):
    estado = 0
    if l == []:
        estado = 'misturado'
    else:
        for i in range(len(l)):
            if l[i]%2==0 and (estado != 'par' or estado != 0):
                estado = 'misturado'
            elif l[i]%2==0 and estado == 0:
                estado = 'par'
            elif l[i]%2!=0 and (estado!= 'impar' or estado != 0):
                estado = 'misturado'
            elif l[i]%2!=0 and estado == 0:
                estado = 'impar'
    print(estado)            
    return estado