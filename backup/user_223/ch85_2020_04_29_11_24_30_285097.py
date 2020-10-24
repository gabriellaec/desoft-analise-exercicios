with open ('macacos-me-mordam.txt') as arquivo:
    conteudo = arquivo.read()
    separado = conteudo.split()
    num_banana=0
    for e in separado:
        palavra_minuscula = lower(e)
        if palavra_minuscula == 'banana':
            num_banana+=1
    print(num_banana)