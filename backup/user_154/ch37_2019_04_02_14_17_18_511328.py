def test_if_primo(test):
    if test < 2 or test % 2 == 0:
        return False
    if test == 2:
        return True
    x = 3
    
    while x < test:
        if (test % x == 0):
            return False
        x = x + 2
    
    return True 

def imprime_primos(n):
    i = 0
    
    while i <= n:
        if (test_if_primo(i) == True):
            print(i)
        i = i + 1
    return