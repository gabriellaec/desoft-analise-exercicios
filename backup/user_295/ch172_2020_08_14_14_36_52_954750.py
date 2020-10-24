
num  = int(input("Nim")

if num >= 0:
    print (imprime_faixa(num))           

def imprime_faixa(n):
    if 0 <= n < 18:
        return("Jovem")
    elif 18 <= n < 60:
        return("Adulto")
    elif n >= 60:
        return("Idoso")
    
    