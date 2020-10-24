def verifica_primo(x):
    i = 2
    while i < x:
        if x%i == 0:
            return False
        
        i += 1
    return True

def primos_entre(a, b): 
    
    i = a 
    soma = 0 
    
    while i <= b:
        if verifica_primo(i):
            soma += 1
        i += 1
    return soma

print(primos_entre(2,100))
        

        