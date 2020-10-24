def remove_vogais(palavra):
    lista_vogais = ["a", "e", "i", "o", "u"]
    strg = []
    i = 0
    while i < len(palavra)-1:
        if palavra[i] not in lista_vogais:
            strg.append(palavra[i])
        i += 1
    return "".join(strg)

print(remove_vogais("batata"))
