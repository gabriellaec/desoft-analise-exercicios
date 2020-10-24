d = float(input("Quantos km:"))

if d <=200:
    p = 0.50*d
else:
    p = 100 + 0.45*(d-200)
    
n1= p
t =2 # Numero de casas
r = int(n1 * 10**t)/10**t
print(r)