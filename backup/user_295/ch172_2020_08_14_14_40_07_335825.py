def imprime_faixa(n):
    if 0 <= n < 18:
        return(print("Jovem"))
    elif 18 <= n < 60:
        return(print("Adulto"))
    elif n >= 60:
        return(print("Idoso"))
    
    