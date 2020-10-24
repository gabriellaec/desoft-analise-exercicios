a = int(input("quantos anos você tem? "))
if a <= 11:
    recebe = "crianca" 
if 12 >= a <= 18:
    recebe = "adolescente"
if a >= 18:
    recebe = "adulto"
return recebe
    