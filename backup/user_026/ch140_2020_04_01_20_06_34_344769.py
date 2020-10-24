def faixa_notas (lista):
    baixo = 0
    medio = 0
    alto = 0
    for nota in lista:
        if nota<5:
            baixo+=1
        elif nota <=7:
            medio+=1
        else:
            alto+=1
    lista2 = [baixo, medio, alto]
    retunr lista2
    