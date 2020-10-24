quant_cig = int(input("Quantos cigarros vc fuma? "))
temp_fumando = int(input("Quantos anos vc fuma? "))
cig_dia = quant_cig*(10/60)/24
temp_perdido = cig_dia*temp_fumando*365
print(temp_perdido)
