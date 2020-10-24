ocorrencias_banana = 0
with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto = arquivo.read()
    for string in texto:
        for l in range(len(string) - 1):
            if string[l] == 'b' or 'B' and string[l + 1] == 'a' or 'A' and string[l + 2] == 'n' or 'N' and string[l + 3] == 'a' or 'A' string[l + 4] == 'n' or 'N' string[l + 5] == 'a' or 'A':
            ocorrencias_banana += 1
    print(ocorrencias_banana)
            