def imprime_faixa(num):
    n = int(num)
    if n < 0:
        print ("nada?")
    if n < 18:
        print ("Jovem")
    elif 18 <= n < 60:
        print ("Adulto")
    elif n >= 60:
        print ("Idoso")
    
    