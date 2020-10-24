with open(macacos_me_mordam.txt, 'r') as arquivo:
    i = 0
    for linha in arquivo:
        for palavra in linha:
            if capitalize(palavra) == 'Banana':
                i += 1
    print(i)