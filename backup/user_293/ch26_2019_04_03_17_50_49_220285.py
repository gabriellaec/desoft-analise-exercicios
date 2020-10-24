dias = int(input("Escreva um numero para dias: "))
horas = int(input("Escreva um numero para horas: "))
minutos = int(input("Escreva um numero para minutos: "))
segundos = int(input("Escreva um numero para segundos: "))
def total_em_segundos(dias,horas,minutos,segundos):
    soma= segundos + (minutos*60) + (horas*60*60) + (dias*60*60*24)
    return soma
print(total_em_segundos(dias,horas,minutos,segundos))