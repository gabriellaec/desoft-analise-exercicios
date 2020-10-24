cigarros=int(input('quantos cigarros voce fuma por dia? '))
anos=int(input('ha quanto tempo voce fuma? '))

         
tempo_perdido_em_um_dia_em_minuto=cigarros*10 
tempo_perdido_ano= tempo_perdido_em_um_dia_em_minuto*365
tempo_perdido_total=tempo_perdido_ano*anos       
tempo_perdido_em_dias=tempo_perdido_total/1440        
print(tempo_perdido_em_dias)
 

