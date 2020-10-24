def dias_perdidos(quantia_de_cigarros, quantia_de_anos):
    dias=((quantia_de_anos*365)*quantia_de_cigarros*10)/1440
    return dias
    
quantia_de_cigarros = input("Quantos cigarros você fuma por dia?")
quantia_de_anos = input("Há quantos anos você fuma?")
print(dias_perdidos)