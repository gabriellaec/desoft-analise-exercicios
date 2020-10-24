def multa(kmh):
    if kmh > 80:
        return 5*(kmh-80)
    
kmh=(int(input("Digite sua velocidade: "))
print (multa(kmh))