def calcula_total_da_nota (preço, quantidade):
    # Cria uma lista onde será adicionados os preços de cada ítem
    nota = []
    # Cria uma variável com a soma dos preços
    total = 0
    i = 0
    # Cria uma condição para o loop i precisa estar nas listas e ambas terão o mesmo tamanho
    while len(preço) == len(quantidade)>i:
        # Define o valor total de cada ítem
        valor = preço[i]*quantidade[i]
        # Adiciona o valor total de cada item a lista de valores
        nota.append(valor)
        # Soma o valor do ítem ao total da nota
        total = total + nota[i]
        i = i + 1
    return total
    