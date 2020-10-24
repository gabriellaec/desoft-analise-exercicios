def nome_usuario(email):
    i = 0
    palavra = []
    for letra in email:
        while email[letra] != "@":
            palavra = palavra+email[letra]
    return palavra
            