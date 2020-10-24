with open('macacos-me-mordam.txt', 'r') as arquivo:
    txt_bananas = arquivo.read()
    txt_maiusculo = txt_bananas.upper()
    lista_maiusculo = txt_maiusculo.split()
    lista_bananas = []
    for i in lista_maiusculo:
        if i == 'BANANA':
            lista_bananas.append(i)

print(len(lista_bananas))
