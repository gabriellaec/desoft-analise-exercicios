def eh_primo(numero):
    if numero%2 == 0:
        return False 
    else:
        return True 
    
def primos_entre(inicio, fim):
    contador = 0 
    numero = inicio 
    while numero <= fim:
        if eh_primo(numero): 
            contador += 1
        numero += 1
    return contador 