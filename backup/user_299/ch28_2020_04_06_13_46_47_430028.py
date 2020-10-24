soma = 0.0
termos = [1]*100
i=0
while i<len(termos):
    lista[i] = 1/(2**i)
    v = lista[i]
    soma += v
    i = i + 1
print(soma)