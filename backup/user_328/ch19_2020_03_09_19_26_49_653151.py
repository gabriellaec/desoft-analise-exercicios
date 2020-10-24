def classifica_triangulo(a1,a2,a3):
    if a1==a2==a3:
        return "equilátero"
    elif (a1==a2 and a1 !=a3) or (a1!=a2 and a2==a3) or (a1==a3 and a2!=a3):
        return "isósceles"
    elif a1!=a2 and a2!=a3 and a1!=a3:
        return "escaleno"