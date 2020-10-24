with open ("churras.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for nome in linhas:
        for num in nome:
            for qnt in num:
                preco = qnt*num
                print(preco)