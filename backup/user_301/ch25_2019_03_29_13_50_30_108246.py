a=int(input('distancia? '))
def calcula(d):
    if d<=200:
        f=d*0.5
    else:
        f=100+(d-200)*0.45
print(calcula(a))