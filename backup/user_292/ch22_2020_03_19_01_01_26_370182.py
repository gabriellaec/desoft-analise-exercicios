fuma_por_dia=int(input('Quantos cigarros voce fuma por dia?'))
x=fuma_por_dia*10
qnt_tempo_fuma=int(input('faz quanto tempo que voce fuma?'))
y=(qnt_tempo_fuma*365*24*60)*fuma_por_dia
dias_perdidos_de_vida=y+x
total_perdido=dias_perdidos_de_vida/1440
print(total_perdido)