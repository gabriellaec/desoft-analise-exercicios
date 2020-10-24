cigarrette = int(input("Quantos cigarros você fuma por dia?"))
time = int(input("Há quantos anos você fuma?"))

time_per_cigarrette = 10 / 60 / 24  # 10 minutes in days
days_in_year = 365

lost_time = cigarrette * time * days_in_year * time_per_cigarrette

print(lost_time)
