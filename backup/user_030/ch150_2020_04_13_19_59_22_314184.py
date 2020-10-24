def calcula_pi(n):
    if n == 0:
        return "Por favor! Digite um nomero valido"
    
    pi = 0
    
    form = list(range(n))
    
    form.remove(0)
    
    for i in (form):
        pi = pi + (6/(i**2))
        
    pi = (pi**(1/2))
    
    return pi