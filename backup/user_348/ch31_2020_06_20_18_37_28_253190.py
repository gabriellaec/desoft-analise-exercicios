def eh_primo (n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range (3, n, 2):
        if (n%2==0):
            return False 
        elif(n%i == 0):
            return False
    else:
        return True

i = 3
def eh_primo (n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    while i < n:
        if (n%2==0):
            return False 
        elif(n%i == 0):
            return False
        i = i + 2
    else:
        return True
