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



def primos_entre(a,b):
    quantidade=0
    p=a
    while a<=p<=b:
        if eh_primo(p):
            quantidade+=1
        p+=1
    return quantidade

a=int(input('primeiro número: '))
b=int(input('segundo número: '))
            
print(primos_entre(a,b))