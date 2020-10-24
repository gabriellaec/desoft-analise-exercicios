potencia = 0
potencia_2 = 1
expressao = float(1/(2**potencia))
expressao_2 = float(1/(2**potencia_2))
soma = expressao + expressao_2
while potencia < 98 and potencia_2 < 99:
    potencia += 1
    potencia_2 += 1
    soma = expressao + expressao_2