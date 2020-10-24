def remove_vogais(frase):
    frase = str(frase)
    frase = frase.lower()
    vogais = ["a", "e", "i", "o", "u"]
    contador = 0
    sem_vogais = ""
    while contador < len(frase):
        if vogais not in frase[contador]:
            sem_vogais += frase[contador]
        contador += 1
    return sem_vogais