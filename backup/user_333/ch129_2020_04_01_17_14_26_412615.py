def verifica_quadrado_perfeito(n):
    i=1 #primeiro numero ímpar
    while n>0:
        n-=i
        i+=2 #variação de ímpares
    if n==0: #se depois das sucessivas subtrações o n for igual a zero é quadrado perfeito
        return True
    else:
        return False