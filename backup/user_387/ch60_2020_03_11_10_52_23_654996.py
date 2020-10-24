def eh_palindromo(a):
    inv = a[-1:-(len(a)+1):-1]
    if inv == a:
        return True
    else:
        return False
      
