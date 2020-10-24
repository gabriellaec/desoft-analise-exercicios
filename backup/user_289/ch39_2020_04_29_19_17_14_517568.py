e = 2
tamanho = 0
while e <= 1000:
    sequencia_collatz = []
    sequencia_collatz.append(e)
    while sequencia_collatz[-1] != 1:
        if sequencia_collatz[-1]%2== 0:
            novo_numero = sequencia_collatz[-1]/2
            sequencia_collatz.append(novo_numero)
        else:
            novo_numero = 3*sequencia_collatz[-1] + 1
            sequencia_collatz.append(novo_numero)
    if len(sequencia_collatz) > tamanho:
        tamanho = len(sequencia_collatz)
        primeiro_elemento = e
    e += 1
print(primeiro_elemento)