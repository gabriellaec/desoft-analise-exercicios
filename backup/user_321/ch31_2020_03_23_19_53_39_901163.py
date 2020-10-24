n = int(input('Insira um número: '))

def eh_primo(n):
    i = 3
    if(n%2==0):
        return False
    else:
        while (i!=n):
            if (n%i==0):
                return False
            else:
                i = i+2
        return True