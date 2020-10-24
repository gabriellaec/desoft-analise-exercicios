def eh_primo(num):
    i = 2 
    if num == 2:
        return True
    elif num == 0 or num == 1:
        return False
    while i < num:
        if num % i == 0:
            return False
        i = i + 1
    return True
def verifica_primos(a):
    dicionario = {}
    p = 0
    c = 0 
    for numero, palavra in dicionario.items():
        if eh_primo(i):
            p = i
            c = True
        else:
            p = i
            c = False
          
       