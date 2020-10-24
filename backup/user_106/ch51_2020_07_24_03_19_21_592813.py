def eh_primo(n):
    if n < 2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        i=3
        while i<n:
            if n%i==0:
                return False
            i+=2
        return True

def primos_entre(a, b):
    lista_p = []
    for i in range(a, b+1):
        if eh_primo(i):
            lista_p.append(i)
    return lista_p


'''
acho que o exc está sendo corrigido de forma errada, considerando que
numeros negativos não podem ser primos. Acredito que o código que resolve a
questão corretamente seja esse (embora não esteja sendo aceito pelo servidor):

def primos_entre(a, b):
    lista_p = []
    p = a
    while p <= b:
        primo = True
        
        if p == 0 or p == 1 or p == -1:
            primo = False
        
        elif p > 1:    
            i = 2 
            while i < p:
                if p % i == 0:
                    primo = False
                    break
                i += 1
        
        else:
            i = -2 
            while i > p:
                if p % i == 0:
                    primo = False
                    break
                i -= 1
        
        if primo:
            lista_p.append(p)
        
        p += 1
    return lista_p

print(primos_entre(-4, 9))
'''