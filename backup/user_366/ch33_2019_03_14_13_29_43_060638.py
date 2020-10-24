termos = 0
soma = 0


while termos < termofinal:
    termofinal = 1/(2**termos)
    termos *= 1/2
    soma += termos

print(soma)