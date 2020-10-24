import churras.txt as arq
i = 1
while i < len(arq):
    custo = arq[i][2] + arq[i-1][2]
    i += 1