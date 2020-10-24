def eh_primo(n):
    if n < 3:
        return True
    for x in range(2,n):
        if n % x == 0:
            return False

print(eh_primo(26))