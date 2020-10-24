def capitaliza (palavra):
    primeira = palavra[0]
    maior = palavra[0].upper()
    palavra.replace(primeira,maior)
    return palavra