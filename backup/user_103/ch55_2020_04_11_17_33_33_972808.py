m = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))

    m.append(linha)

maior_linha = 0
maior_coluna = 0
maior = m[0][0]
for l in range(4):
    for c in range(4):        
        if maior < m[l][c]:
            maior = m[l][c]
            maior_linha = l
            maior_coluna = c
        