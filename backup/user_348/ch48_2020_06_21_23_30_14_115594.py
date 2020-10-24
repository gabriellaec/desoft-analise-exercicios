def eh_crescente(lista):
    # Cria variáveis condicionais
    crescente = True
    decrescente = True
    i = 1
    # Cria a condição para o loop
    while i < len(lista):
        # Condição para ser crescente
        if lista[i] >= lista[i-1]: 
            decrescente = False
        # Condição para ser decrescente
        if lista[i] <= lista[i -1]:
            crescente = False
        i = i + 1
    # Se a lista for crescente
    if crescente:
        return True
    # Se a lista for decrescente
    else: 
        return False