def eh_primo(num):
    a=3
    if num==0 or num==1:
        return False
    elif num==2 or num==3:
        return True
    elif num%2==0:
        return False
    else:
        while a<num:
            if num%a==0:
                resto = num%a
                break
            else:
                resto = num%a
                a=a+2
        if resto ==0:
            return False
        else:
            return True

def primos_entre(a,b):
    contador=0
    for i in range(a,b+1):
        if eh_primo(i):
            contador+=1
    print(contador)