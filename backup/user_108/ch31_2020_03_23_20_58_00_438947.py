def eh_primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
		x = 2
        while x <= n:
            if n % x == 0:
                return False
      	return True