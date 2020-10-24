def verifica_preco(titulo, dicionario, tabela):
    elemento1 = titulo
    dicionario2 = dicionario.keys()
    for i in range len(dicionario)-1:
        if dicionario[i][0] == titulo:
            print("A cor é: {0}". format(tabela[i][1]))

            
        
