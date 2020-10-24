with open ("churras.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for nome in linhas:
        for nome in quantidade:
            for quantidade in preco:
                k = quantidade*preco
                print(k)