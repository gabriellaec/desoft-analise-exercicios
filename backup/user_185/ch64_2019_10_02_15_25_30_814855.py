def pos_arroba(nome):
    tamanho = len(nome)
    contador = 0
    posição = "Não tem @"
    while contador <= tamanho:
        corte = nome[ contador - 1 : contador]
        if corte == "@":
            posição = nome.find("@")
        contador = contador + 1
    print(posição)
    return posição

pos_arroba("rafael@gmail.com")

def nome_usuario(e_mail):
    posi = pos_arroba(e_mail)
    b = 1
    soma = ""
    while b <= posi:
        c = e_mail[ b - 1 : b]
        soma = soma + c
        b = b + 1
    return soma

