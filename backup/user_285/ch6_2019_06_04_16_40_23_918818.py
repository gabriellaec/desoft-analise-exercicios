def encontra_maximo(matriz):
    maior=0
    for linha in matriz:
        for elemento in linha:
            if abs(elemento) > maior:
                maior=abs(elemento) 
    return maior

        