def maior_primo_menor_que(n):
    if n>1:
        def eh_primo (n):
            if n==1 or n==0:
                return False
            elif n==2:
                return True
            elif n>2:
                if n%2==0:
                    return False
                else:
                    y=3
                    a=True
                    while a:
                        if n>y and n%y==0:
                            return False
                        elif n==y:
                            return True
                            a=False
                        y=y+2
        if eh_primo(n) == True:
            return n
        else:
            while eh_primo == False:
                n-=1
            return n
    else:
        return -1
            