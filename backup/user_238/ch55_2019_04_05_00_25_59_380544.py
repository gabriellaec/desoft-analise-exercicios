def eh_primo(n):
    if n <=1:
        return False
    for e in range(2,n):
        if (n % e == 0):
      		  return False
    return True

def primos_entre(a,b):
        i=a
        lista=[]
        while i < b:
            primo=eh_primo(i)
            if primo is True:
                lista.append(i)
            i+=1
        return lista
print(primos_entre(1,8))
            
            