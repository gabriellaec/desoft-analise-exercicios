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
def imprime_primo(n):
    if eh_primo == 
