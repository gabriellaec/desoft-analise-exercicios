def remove_vogais(frase):
    vogais = "aeiou"
    contador = 0
    sem_vogais = ""
    while contador < len(frase):
        if vogais not in frase[contador]:
            sem_vogais += frase[contador]
        contador += 1
    return sem_vogais