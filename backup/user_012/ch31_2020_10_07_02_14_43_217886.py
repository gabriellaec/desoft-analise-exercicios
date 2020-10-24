def eh_primo(p):
    if p == 0: 
        return False 
    elif p == 1:
        return False 
    elif p == 2:
        return True
    elif p == 3:
        return True
    elif p % 2 == 0: # o primo só pode ser divisível por 1 e por ele mesmo. Logo, se oresto da divisão por 2, for 0, ele não é primo(ou seja todos os pares com a excesão do 2 não são primos)
        return False
    if p > 3: # para checar se os números impares são primos, eu tenho que checar se estes impares divididos por 3 só dividem por eles mesmos
        i=3
        while i < p:
            if p%i != 0: # o números que definir dividido por i(meu contador que pula de dois em dois, onde me dar só os impares) for diferente de zero é primo
                i=i+2
    
            else:
                return False # logo se for divisível por qualquer outro impar, ele não é primo
    
    return True
    