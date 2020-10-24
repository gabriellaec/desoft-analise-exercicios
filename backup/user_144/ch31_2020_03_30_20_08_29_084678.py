def eh_primo(n):
    contador = 1
    while contador <= n:
        if n%2==1:
            contador=contador+1
            return True
        elif n == 0 or n==1:
            return False
        
        else:
            return False