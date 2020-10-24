def imprime_faixa(n):
    if n < 0:
        print ("nada?")
    if n < 18:
        print ("Jovem")
    elif 18 <= n < 60:
        print ("Adulto")
    elif n >= 60:
        print ("Idoso")
    
    