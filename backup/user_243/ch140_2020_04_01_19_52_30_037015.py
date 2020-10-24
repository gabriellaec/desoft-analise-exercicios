def faixa_notas(lista):
    nota=len(lista)
    inferior=0
    entre=0
    maior=0
    for nota in lista:
        if nota<5:
            inferior=inferior+1   
        elif nota<=7:
            entre=entre+1
        else:
            maior=maior+1
    notasfinais=[inferior,entre,maior]
    return notasfinais
