def eh_primo (n):
    contador = 1
    while contador <= n:
        if n%2==1:
            contador=contador+1
            return True
        else:
            return False
