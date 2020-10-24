quantidade_por_dia= int(input("numeros de cigarros por dia ?"))
anos= int(input("por quantos anos")) 
if quantidade_por_dia >= 1:
    minutos_perdidos= quantidade_por_dia*10*365*anos
    horas_perdidos = minutos_perdidos/60
    dias_perdidos= horas_perdidas/24
else:
    dias_perdidos= 0
    
print(dias_perdidos)
 