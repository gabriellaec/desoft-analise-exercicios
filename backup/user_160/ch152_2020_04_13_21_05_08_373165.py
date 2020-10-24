def verifica_preco(titulo, dicionario, tabela):
    elemento1 = titulo
    dicionario2 = dicionario.keys()
    cor = branco
    for i in range len(dicionario)-1:
        if dicionario[i][0] == titulo:
            cor = dicionario[0][i]
        if cor == tabela[i][0]:
            print("O valor é: {0}". format(tabela[0][i]))

            
        
