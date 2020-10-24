def calcula_euler(x,n):
    e_x = 1 + x
    for i in range(2, n, 1):
        e_x = e_x + (x^2)/(x!)    
    
    #calculos
    return e_x