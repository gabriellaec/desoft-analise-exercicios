def eh_primo(num):
    n=3
    while n<num:
        if num%2==0 or num%n==0:
            return False
        n+=2
    if num==0 or num==1:
        return False
    
    else:
        return True
def maior_primo_menor_que: 
    for i in range(1,n,-1):
            if eh_primo == True:
                return i
    else:
        return -1
        