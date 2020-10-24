def multa(kmh):
    if kmh > 80:
        resultado= 5.00*(kmh-80.00)
        return str(resultado ) + 'de multa'
    else:
        return 'Não foi multado'
    
velocidade=(int(input("Digite sua velocidade: "))
final=multa(kmh)
print (final)