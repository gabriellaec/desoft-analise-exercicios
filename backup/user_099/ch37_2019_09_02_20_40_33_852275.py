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

def lista_primos(n):
    contador=0
    num=1
    nums=[]
    while contador<n:
        if eh_primo(num):
            nums.append(num)
            contador+=1
            num+=1
        else:
            num+=1
    return nums