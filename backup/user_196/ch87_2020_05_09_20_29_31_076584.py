with open ("churras.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linhas in nome:
        for nome in quantidade:
            for quantidade in preco:
                k = quantidade*preco
                print(k)