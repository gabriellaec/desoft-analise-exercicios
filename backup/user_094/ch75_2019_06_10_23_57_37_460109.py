def verifica_primos(x):
    dic = {}
    for n in x:
        if n==1 or n==0: 
            dic[n] = False
         #   return False
        elif n==2 or n==3:
            dic[n] = True
           # return True
        elif n%2==0:
            dic[n] = False
          #  return False
        i=3
        while i<n:
            if n%i==0:
                dic[n] = False
          #      return False
            i+=2
        dic[n] = True
      #  return True