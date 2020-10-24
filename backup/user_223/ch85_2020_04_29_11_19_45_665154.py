with open ('macacos-me-mordam.txt') as arquivo:
    conteudo = arquivo.read
    separado = conteudo.split()
    num_banana=0
    for e in separado:
        if e =='banana'.lower:
            num_banana+=1
    return num_banana