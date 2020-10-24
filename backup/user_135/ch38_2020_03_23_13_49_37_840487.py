def quantos_uns(num):
    termos = 0
    contador = 0
    num = input()
    while termos < len(num):
        if num[termos] == 1:
            contador = contador + 1
            termos = termos + 1
        else:
            termos = termos + 1