def tempo_perdido(a,b):
 return ((10*b)*(a*365))/1440

a=int(input("digite o numero de cigarros:"))
b=int(input("digite o numero de anos fumados:"))
e=(tempo_perdido(a,b))
print(e)