def testa_primo(x):
    if x%2 and x%3:
        return False
    elif x%x and x%1:
        return True
    
def maior_primo_menor_que(x):
    if x < 0:
        return -1
    while x >= 0:
        if testa_primo(x)==True:
            return x
        elif testa_primo(x)==False:
            return "deu ruim"
            
            
            
        
    