dia=int(input("Quantos dias:"))
h = int(input("Que horas são:"))
m = int(input("Quantos min:"))                
s = int(input("Quantos segundos:"))
      
total_segundos = dia*86.400 + h*360 + m*60 + s
      
print(total_segundos)