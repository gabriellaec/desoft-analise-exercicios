with open ('macacos-me-mordam.txt') as arquivo:
    conteudo = arquivo.read()
    separado = conteudo.split()
    num_banana=0
    for e in separado:
        if e ==lower('banana'):
            num_banana+=1
    print(num_banana)