def raiz_quadrada(x):
    impar =1
    w = x
    ct =0
    while w>0:
        w= w-impar
        ct =ct+1
        impar+=2
    return ct
    