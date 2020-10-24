with open("macacos-me-mordam.txt", 'r') as arquivo:
    conteudo=arquivo.readline()
    banana=0
    if "banana" in conteudo:
        banana=1+banana
    print(banana)    
        