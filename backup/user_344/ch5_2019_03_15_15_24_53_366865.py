def eh_primo(num):
    contador= 2
    if num==1 or num==0:
        return False
    while contador<num:
        if num%contador==0:
            return False
        if contador==2:
            contador+=1
        else:
            contador+=2
    return True 
def maior_primo_menor_que(n):
    if n<=1:
        return -1
    while eh_primo(n) == False:
        n-=1
    return n
        
        
        
        
    