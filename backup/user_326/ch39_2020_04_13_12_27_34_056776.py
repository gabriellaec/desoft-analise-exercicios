maoir_numero_de_operacoes = 0
for numero in range(2, 1000):
    qunatidade_de_operações = 0
    numero_checado = numero
    while numero_checado != 1:
        if numero_checado % 2 == 0:
            numero_checado /= 2
            qunatidade_de_operações += 1
        else:
            numero_checado = 3*numero_checado + 1
            qunatidade_de_operações += 1
    if qunatidade_de_operações > maoir_numero_de_operacoes:
        maoir_numero_de_operacoes = qunatidade_de_operações
        numero_resposta = numero

print(numero_resposta)