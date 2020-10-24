def calcula_total_da_nota (prices, quantityes):
    total = 0
    
    i = 0
    while i < len(prices):
        price = prices[i]
        quantity = quantityes[i]
        
        total += price * quantity
        
        i += 1
        
    return total
