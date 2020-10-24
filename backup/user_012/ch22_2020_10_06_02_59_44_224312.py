cigarros= int(input('Quantos cigarros você fuma por dia: '))
anos= int(input('Fuma a quantos anos: '))

dias= anos*365
total=cigarros*dias #total de cigarros
t_minutos= 10*total # tempo perdido em minutos
t_horas= t_minutos/60 # tempo perdido em horas
t_dias= t_horas/24



print(f'você perdeu {t_dias} dias de sua vida')
