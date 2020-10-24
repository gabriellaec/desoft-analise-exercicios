def eh_primo(x):
  impar = 1
  while x != impar:
    impar += 2
    if x == 1:
      return False
    elif x % 2 == 0:
      return False
    elif x % impar == 0 and x != impar:
      return False
    else:
      return True