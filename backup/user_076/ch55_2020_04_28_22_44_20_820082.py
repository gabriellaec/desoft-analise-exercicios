def encontra_maximo (matriz):
    máximo = matriz[0][0]
    for linha in matriz:
        i = 0
        while i+1<len(linha):
            if linha[i+1]>linha[i]:
                máximo = linha[i+1]
            i+=1
    return máximo