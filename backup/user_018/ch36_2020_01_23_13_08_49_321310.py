i=1
def eh_primo(n):
    if n == 0 or n == 1:
        return 'False'
    elif n%2 == 0:
        return 'False'
    else:
        return 'True'
    while i <= n :
        if i%n == 0:
            return 'False'
        else: 
            return 'True'
        i += 1