def verifica_numero(num):
    for i in range(num):
        if i == sum(int(x) ** int(x) for x in str(i)) or i > 1:
            return True
        
        else:
            return False
    
    