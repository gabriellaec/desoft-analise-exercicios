def calcula_total_da_nota(price, items):
    n = len(price)
    i=0
    total=0
    
    while i < n:
        a=price[i]
        b=items[i]
        total=total+a*b
        i=i+1
    return total