def maior_primo_menor_que(n):
    i=n
primo=0
while(primo<n):
    if(primo%primo==0 and primo%1==0):
        return True
       i-=primo
    else:
        =-1
        return False
   