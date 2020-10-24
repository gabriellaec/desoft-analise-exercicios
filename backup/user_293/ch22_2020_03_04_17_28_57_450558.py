cig_dias = int(input("Quantos cigarros vc fuma por dia? "))
cig_anos = int(input("Há quantos anos vc fuma? "))

total_perdido = cig_dias*0.00694444
total_anos_dias = cig_anos*365
total_cig = total_perdido*total_anos_dias
print(total_cig)