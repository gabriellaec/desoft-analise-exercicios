quant = int(input("n de cigarros fumados por dia: "))
anos = int(input("n de anos que passaram desde que começou a fumar: "))
anos_em_dias = anos * 365
tempo_perdido= anos_em_dias *quant *0.694444444
print (tempo_perdido)