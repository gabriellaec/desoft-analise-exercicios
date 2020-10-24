ocorrencias_banana = 0
with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto = arquivo.read()
    for string in texto:
        if string == 'banana':
            ocorrencias_banana += 1
    print(ocorrencias_banana)
            