e = 2
tamanho = 0
while e < 1001:
    sequencia_collatz = []
    sequencia_collatz.append(e)
    i = 0
    while sequencia_collatz[-1] != 1:
        if sequencia_collatz[i]%2== 0:
            novo_numero = sequencia_collatz[i]/2
            sequencia_collatz.append(novo_numero)
            i += 1
            e += 1
        else:
            novo_numero = 3*sequencia_collatz[i] + 1
            sequencia_collatz.append(novo_numero)
            i += 1
            e += 1
    if len(sequencia_collatz) > tamanho:
        tamanho = len(sequencia_collatz)