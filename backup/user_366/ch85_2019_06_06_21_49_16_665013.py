arquivo = open("macacos-me-mordam.txt", "r")
quantidade = 0
for linha in arquivo.readlines():
    a = linha.upper()
    i = 0
    while i < len(a):
        if a[i:i+6] == "BANANA":
            quantidade += 1
        i += 1
print(quantidade)
arquivo.close()