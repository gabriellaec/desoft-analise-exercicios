def eh_primo(n):
    d = 2
    while d<n:
        if n % d == 0:
            return False
        else:
            d += 1
    return True 
def primos_entre(a,b):
    f=0
    while f<a:
      f+=1
    while f<=b:
        if eh_primo(f) == True:
            print(f)
        f+=1