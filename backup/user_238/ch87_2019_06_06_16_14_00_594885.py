soma=0
with open ("churras.txt","r") as arquivo:
    linhas=arquivo.readlines()
    for linha in linhas:
        lista = linha.split(",")
        quantidade=int(lista[1])
        valor=float(lista[2])
        soma += quantidade*valor
        
print(soma)
        