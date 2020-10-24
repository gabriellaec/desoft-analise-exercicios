a = int (input ("Quantos cigarros você fuma por dia?"))
b = int (input ("Há quanto tempo você fuma?"))
           
total_cigarros = (b*365)* a
dias_perdidos = (total_cigarros * 10)/24

print ("Você perdeu", dias_perdidos, "de vida")