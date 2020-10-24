def eh_primo(num):
    if num == 2:
      return True
    elif num == 1 or num == 0:
      return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def verifica_primos(lista=[]):
  dic = {}
  for i in lista:
    dic[i] = eh_primo(i)
  return dic