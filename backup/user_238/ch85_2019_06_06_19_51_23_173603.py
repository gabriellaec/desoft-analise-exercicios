with open ("macacos-me-mordam.txt","r") as f:
    n=0
    linhas=f.readlines()
    linhas.lower()
    for linha in linhas:
        palavra=linha.split()
        for p in palavra:
            if p == "banana":
                n+=1
    print(n)