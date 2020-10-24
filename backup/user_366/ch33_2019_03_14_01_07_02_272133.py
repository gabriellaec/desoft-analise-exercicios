termos = 1
soma = 1
termofinal = 1/(2**99)

while termos < termofinal:
    termos *= 1/2
    soma += termo

print(soma)