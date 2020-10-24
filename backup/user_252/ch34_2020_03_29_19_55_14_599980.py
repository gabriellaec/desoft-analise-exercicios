def maior_primo_menor_que(n):
    if n>1:
        def eh_primo(n):
            i=3
            if n==2 or n==3:
                return True
            elif n%2==0:
                return False 
            else:
                while n%i!=0 and n>1:
                    i+=2
                if n==i:
                    return True 
                else:
                    return False
        if eh_primo(n)==True:
            return n
        else:
            while eh_primo(n)==False:
                n-=1
            return n
    else:
        return -1
         