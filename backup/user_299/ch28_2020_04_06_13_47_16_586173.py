soma = 0.0
termos = [1]*100
i=0
while i<len(termos):
    termos[i] = 1/(2**i)
    v = termos[i]
    soma += v
    i = i + 1
print(soma)