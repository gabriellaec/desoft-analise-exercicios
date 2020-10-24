def faixa_notas(lista):
    abaixo=0
    media=0
    acima=0
    for a in lista:
        if a<5:
            abaixo=abaixo+1
        elif a<=7:
            media=media+1
        else:
            acima=acima+1
    return [abaixo,média,acima]
    
            