def valor_da_passagem(km):
    if km<=200:
        p=0.5*km
        return p
    else:
        p=0.5*km+0.45*(km-200)
      	return p