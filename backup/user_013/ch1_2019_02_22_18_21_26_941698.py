def calcula_valor_devido(e,j,n):  
    c = round( e * ( 1 + j/100) ** n, 2)
    return c
