def verifica_quadrado_perfeito(n)
m=n
p=2
while m>=0:
    p= p-2
    m= m-p
    if m**2=n:
        return True
    else return False 
