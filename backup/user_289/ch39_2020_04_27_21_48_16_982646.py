i = 0
tamanho = 0
for numero in range(0, 1000):
    sequencia_collatz = []
    sequencia_collatz[0] = numero
    while sequencia_collatz[-1] != 1:
        if numero%2== 0:
            novo_numero = sequencia_collatz[i]/2
            sequencia_collatz.append(novo_numero)
            i += 1
        else:
            novo_numero = 3*numero + 1
            sequencia_collatz.append(novo_numero)
            i += 1
    if len(sequencia_collatz) > tamanho:
        tamanho = len(sequencia_collatz)