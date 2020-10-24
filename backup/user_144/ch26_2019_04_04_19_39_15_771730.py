d = int(input("Quantos dias? "))
h =int(input("Quantos horas? "))
m =int(input("Quantos minutos? ")) 
s=int(input("Quantos segundos? ")) 
        
        
d = d * 86400
h = h *3600
m = m * 60

y = d + h + m + s
print(y)
