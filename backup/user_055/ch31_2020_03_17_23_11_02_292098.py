n = int(input('Digite um número: ')) 
def eh_primo(n):
    x = 3
    if n % 2 == 0 and n != 2 or n == 0 or n == 1:
        return False
    while n > x:
        if n % x == 0:
            return False
        x += 2
    else:
        return True
eh_primo(n)
