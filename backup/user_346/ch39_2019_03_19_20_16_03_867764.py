ON=True
contador=0
while ON:
    numero=int(input())
    if numero==0:
        ON=False
    else:
        contador+=numero
print(contador)
        