dia= int(input("Insira dia:"))

hr= int(input("Insira hora:"))

m= int(input("Insira minutos:"))

seg= int(input("Insira segundos:"))

def segundos (dia,hr,m,seg):
    res= seg+ m*60 +hr*3600+dia*24*60*60
    return res

resposta= segundos(dia,hr,m,seg)

print("Total de segundos: {0}".format(resposta))