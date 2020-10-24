def eh_primo(numero):
    if numero==1 or numero==0:
        return False
    elif numero==2:
        return True
    else:
        x=3
        while x<numero:
            if numero%x==0:
                break #serve para sair do while
            else:
                x+=2
        if numero==x:
            return True
        else:
            return False
        
def maior_primo_menor_que(n):
    r=0
    if n<=1:
        r=-1
    else:
        primo=eh_primo(n)
        while primo==False:
            primo=eh_primo(n)
            if primo:
                r=n
            else:
                n-=1
    return r