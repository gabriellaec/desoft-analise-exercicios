def pos_arroba(nome):
    tamanho = len(nome)
    contador = 0
    while contador <= tamanho:
        corte = nome[ contador - 1 : contador]
        if corte == "@":
            posição = nome.find("@")
        contador = contador + 1
    print(posição)
    return posição