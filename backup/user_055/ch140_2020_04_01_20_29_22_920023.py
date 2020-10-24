def faixa_notas(notas):
    lista = []
    inferior = []
    media = []
    cabeca = []
    x = 0.5
    while x < len(notas):

        if x < 5:
            inferior.append(x)
            

        if x > 5 and x > 7:
            media.append(x)
            
            
        if x > 7:
            cabeca.append(x)
    
    x += 0.5
            
    lista.append(len(inferior))
    lista.append(len(media))
    lista.append(len(cabeca))
    return lista