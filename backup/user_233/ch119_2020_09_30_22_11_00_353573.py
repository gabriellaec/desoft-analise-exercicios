# sem fazer uso de for loop

def fatorial(n):
    ''' retorna o fatorial de "n" '''
    
    # retorna 1 para n = 0
    if n == 0: return 1
    
    # variável de contagem
    contagem = 0
    
    # variável base de multiplicação
    fatorial = 1
    
    # loop de multiplicação
    while contagem <= n:
        fatorial *= contagem
        contagem += 1
    
    # retorno de fatorial
    return fatorial


def calcula_euler(x, n):
    ''' calcula o número de Euler aproximado
        a partir da série de Taylor de "n" valores '''
    
    # variável base para as somas
    euler = 0
    
    # variável de contagem do loop
    contagem = 0
    
    # loop de soma
    while contagem < n:
        
        # soma
        euler += 1 / fatorial(contagem)
        
        # incremento da variável de contagem
        contagem += 1
        
    return euler


