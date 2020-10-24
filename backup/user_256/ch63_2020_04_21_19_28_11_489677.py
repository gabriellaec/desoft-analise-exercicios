def nome_usuario(email):
    i = 0
    for letra in email:
        while email[letra] != "@":
            palavra = palavra+email[letra]
    return palavra
            