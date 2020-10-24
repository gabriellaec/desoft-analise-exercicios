def raiz_quadrada(n):
    proximoNumero=n
    impar=1
    raiz=0
    while(impar<=proximoNumero):
        proximoNumero-=impar
        impar+=2
        raiz+=1
    return raiz
    