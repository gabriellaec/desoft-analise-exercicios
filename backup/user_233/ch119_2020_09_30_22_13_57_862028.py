# sem fazer uso de for loop

def fatorial(n):
    ''' retorna o fatorial de "n" '''
    
    # variável de contagem
    contagem = 0
    
    # variável base de multiplicação
    fatorial = 1
    
    # loop de multiplicação
    while contagem < n:
        contagem += 1
        fatorial *= contagem
    
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
        euler += x ** contagem / fatorial(contagem)
        
        # incremento da variável de contagem
        contagem += 1
    
    # retorna a soma elevada a "x"
    return euler ** x


