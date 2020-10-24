quantidade_por_dia= int(input("numeros de cigarros por dia ?"))
anos= int(input("por quantos anos")) 
minutos_perdidos= quantidade_por_dia*10*365*anos
horas_perdidos = minutos_perdidos/60
dias_perdidos= horas_perdidos/24
    
print(dias_perdidos)
 