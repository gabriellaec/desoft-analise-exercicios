# Convertendo libras para quilogramas
# Fator de conversão: 1 libra = 0,453592 kg

def libras_para_kg(peso_libras):
    peso_kg = 0,453592*peso_libras
    return peso_kg

massa_libra = 17
massa_kg = libras_para_kg(massa_libra)

print(massa_kg)