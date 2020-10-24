def encontra_maximo(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[0][2]
    d = matriz[1][0]
    e = matriz[1][1]
    f = matriz[1][2]
    g = matriz[2][0]
    h = matriz[2][1]
    i = matriz[2][2]
    return (a*e*i + b*f*g + c*d*h) - (a*f*h + b*d*i + c*e*g)