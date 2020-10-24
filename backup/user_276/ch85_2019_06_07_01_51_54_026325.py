with open(macacos_me_mordam.txt, 'r') as arquivo:
    conteudo = arquivo.read()
    i = 0
    for linha in conteudo:
        for palavra in linha:
            if capitalize(palavra) == 'Banana':
                i += 1
    print(i)