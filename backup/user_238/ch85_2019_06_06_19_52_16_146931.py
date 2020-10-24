with open ("macacos-me-mordam.txt","r") as f:
    n=0
    linhas=f.readlines()
    for linha in linhas:
        palavra=linha.split()
        linha.lower()

        for p in palavra:
            if p == "banana":
                n+=1
    print(n)