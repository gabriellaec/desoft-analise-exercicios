def eh_primo(n):
    if n < 2:
        return False
    ellif n == 2:
        return True
    else:
		x = 2
        while x < n:
            if n % x:
                return False
      	return True