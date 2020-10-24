dia=int(input("Quantos dias:"))
h = int(input("Que horas são:"))
m = int(input("Quantos min:"))                
s = int(input("Quantos segundos:"))
      
total_segundos = dia*86400 + h*3600 + m*60 + s
      
print(total_segundos)