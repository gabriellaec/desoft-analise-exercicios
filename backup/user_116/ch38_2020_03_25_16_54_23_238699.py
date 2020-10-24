def quantos_un(n):
    c=len(n)
    contador=0
    numeros_de_um=0
    while contador<c:
        if n[contador] == ("1"):
            numeros_de_um+=1
            contador+=1
        else:
            contador+=1
    return numeros_de_um
