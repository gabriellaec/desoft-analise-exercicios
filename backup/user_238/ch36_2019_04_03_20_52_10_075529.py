def eh_primo(numero):
    if n <=1:
        return False
    for e in range(2,n):
        if (n % e == 0):
      		  return False
    return True