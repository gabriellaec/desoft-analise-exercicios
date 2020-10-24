def separa_trios (lista):
    # Cria uma lista onde os trios serão adicionados
    trio = []
    # Determina o primeiro índice a ser analisado
    i = 0
    # Cria a condição para o loop
    while i < len(lista):
        # Cria uma variável com o trio (do índice atual até 2 depois)
        alunos = lista[i: i + 3]
        # Adiciona o trio atual à lista de trios
        trio.append(alunos)
        # O índice vai de 3 em 3
        i = i + 3
    return trio