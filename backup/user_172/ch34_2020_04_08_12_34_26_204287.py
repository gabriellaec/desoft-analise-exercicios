def maior_primo_menor_que(n):
    if n>1:
        def eh_primo (n):
            if n==2 or n==3:
                return True
            elif n%2==0:
                return False
            else:
                y=3
                while n%y!=0 and n>y:
                    y+=2
                if n==y:
                    return True
                else:
                    return False
        if eh_primo(n) == True:
            return n
        else:
            while eh_primo == False:
                n-=1
            return n
    else:
        return -1
            