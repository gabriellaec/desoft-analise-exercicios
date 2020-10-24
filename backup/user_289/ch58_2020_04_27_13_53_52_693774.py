def conta_a(string):
    palavra = str(string)
    n_vezes = 0
    for letra in palavra:
        if letra == 'a':
            n_vezes += 1
    return n_vezes
      