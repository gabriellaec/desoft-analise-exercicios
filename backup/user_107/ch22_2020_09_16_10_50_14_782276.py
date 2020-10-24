count = int(input("Quantos cigarros você fuma por dia?"))
time = int(input("Há quantos anos você fuma?"))

days_per_cigarrette = 10 / 60 / 24

lost_time = count * days_per_cigarrette * time
