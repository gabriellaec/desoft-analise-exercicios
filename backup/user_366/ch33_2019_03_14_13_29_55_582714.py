termos = 0
soma = 0


while termos < 100:
    termofinal = 1/(2**termos)
    termos *= 1/2
    soma += termos

print(soma)