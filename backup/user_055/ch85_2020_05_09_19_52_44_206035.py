ocorrencias_banana = 0
with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto = arquivo.read()
    for string in texto:
        for l in range(len(string) - 1):
            if string[l] == 'b' or string[l] == 'B' and string[l + 1] == 'a' or string[l + 1] == 'A'\
                and string[l + 2] == 'n' or string[l + 2] == 'N' and string[l + 3] == 'a' or string[l + 3] == 'A'\
                and string[l + 4] == 'n' or string[l + 4] == 'N' and string[l + 5] == 'a' or string[l + 5] == 'A':
                ocorrencias_banana += 1
    print(ocorrencias_banana)
            