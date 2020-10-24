def primo(p):
    a=2
    while a < p:
        if p%a==0:
            return False
        a+=1
    return True    
print(primo(13))    
    
def primos_entre(a, b):
    i=a
    soma=0
    while i <= b:
        if primo(i):
            soma +=1
        i+=1
    return soma    
a=2
b=100
print(primos_entre(a, b))
        