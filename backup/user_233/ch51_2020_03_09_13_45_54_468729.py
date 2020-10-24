def eh_primo(n):
    
    if n == 2: return True
    if n % 2 == 0: return False
    
    final = int(n / 2) + 1
    if final % 2 == 0: final = int(n / 2)
    
    for impar in range(3, final, 2):
        if n % impar == 0: return False
    
    return True



def primos_entre(a, b):
    
    resultado = list()
    
    if b <= 0: return []
    if a < 0: a = 0
        
    if a <= 2 and b >= 2: resultado.append(2)
    
    inicial = a
    if a % 2 == 0: inicial = a + 1
    
    final = b + 1
    if b % 2 == 0: final = b
    
    for numero in range(inicial, final, 2):
        if eh_primo(numero): resultado.append(numero)
    
    return resultado
            
            