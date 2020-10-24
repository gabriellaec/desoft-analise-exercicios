def capitaliza (palavra):
    primeira = palavra[0]
    maior = palavra[0].upper() + palavra[1:]
    x=palavra.replace(primeira,maior)
    return palavra