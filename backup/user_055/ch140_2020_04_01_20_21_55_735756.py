def faixa_notas(notas):
    lista = []
    inferior = []
    media = []
    cabeca = []
    for x in notas:
        while x < 5:
            inferior.append(x)
   
        while x > 5 and x > 7:
            media.append(x)
            
        while x > 7:
            cabeca.append(x)

    lista.append(len(inferior))
    lista.append(len(media))
    lista.append(len(cabeca))
    return lista