def apaga_repetidos(string):
    lista_todas=[]
    #verifica todos os caracteres
    for letra in string:
        #verifica se letra(independete de seu estado(maiusculo/minusculo)) esta na lista
        if letra.lower() in lista_todas or letra.upper() in lista_todas:
            #substitui letra pelo asterisco
            lista_todas.append('*')
        else:
            #adiciona letra
            lista_todas.append(letra)
    #base da palavra a ser criada
    palavra=''
    #junta cada letra aa palavra
    for element in lista_todas:
        palavra+=element
    #retorna a palavra recem formada
    return palavra