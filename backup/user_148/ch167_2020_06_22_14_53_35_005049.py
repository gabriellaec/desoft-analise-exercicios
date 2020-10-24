def bairro_mais_custoso(dicionario):

dicionario2 = {}
for k in dicionario:
    for v in range(6, 12):
        if not k in dicionario2:
            dicionario2[k] = dicionario[k][v]
        else:
            dicionario2[k] += dicionario[k][v]

for k, v in dicionario2:
    s = sum(v)
    if k = max(s):
        return k
        