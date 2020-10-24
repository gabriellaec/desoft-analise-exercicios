def multa(kmh):
    if kmh > 80:
        return 5.00*(kmh-80.00)
    else:
        return 'Não foi multado'
    
kmh=(int(input("Digite sua velocidade: "))
print (multa(kmh))