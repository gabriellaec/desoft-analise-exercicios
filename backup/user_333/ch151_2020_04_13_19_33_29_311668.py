def classifica_lista(lista):
    if len(lista)<2:
        resultado='nenhum'
    else:
        if lista[0]<lista[1]:
            resultado='crescente'
        elif lista[0]>lista[1]:
            resultado='decrescente'
        else:
            resultado='nenhum'
        for i in range(1,len(lista)-1):
            if lista[i+1]<lista[i] and resultado=='decrescente':
                resultado='decrescente'
            elif lista[i+1]<lista[i] and resultado=='crescente':
                resultado='nenhum'
                break
            elif lista[i+1]>lista[i] and resultado=='decrescente':
                resultado='nenhum'
                break
            elif lista[i+1]>lista[i] and resultado=='crescente':
                resultado='crescente'
            else:
                resultado='nenhum'
                break
    return resultado
            