def eh_primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    for x in range(2,n):
        if n % x == 0:
            return False
	return true

print(eh_primo(26))