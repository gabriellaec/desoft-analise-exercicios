with open("macacos-me-mordam.txt","r") as arquivo :
    ler=arquivo.read()
    tudo_minusculo=ler.lower()
    contar=tudo_minusculo.count("banana")
print(contar)