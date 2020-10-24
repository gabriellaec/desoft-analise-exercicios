def calcula_salario (s):
    a = 0 
    if s > 1250:
        a = s*0.10 + s
    else:
        a = s*0.15 + s  
    return s
    
    