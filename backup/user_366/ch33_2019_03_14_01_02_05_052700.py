termos = 1
soma = 0
termofinal = 1/(2**99)

while termos < termofinal:
    termos *= 1/2
    soma += primeirotermo

print(soma)