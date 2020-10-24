cigarrette = int(input("Quantos cigarros você fuma por dia?"))
time = int(input("Há quantos anos você fuma?"))

time_per_cigarrette = 10 / 60 / 24  # 10 minutes in days

lost_time = cigarrette * time * time_per_cigarrette
