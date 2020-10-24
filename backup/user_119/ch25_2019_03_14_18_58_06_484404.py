def preco_km(km):
    if km<=200:
        return km*0.5
    else:
        return 100+(km-200)*0.45