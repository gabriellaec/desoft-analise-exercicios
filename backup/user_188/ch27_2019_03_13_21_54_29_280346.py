def vida(num_cig, anos):
    dias = anos * 365
    min_perdidos = num_cig * dias * 10
    tempo_horas = tempo_min / 60
    tempo_dias = tempo_horas / 24
    return tempo_dias

cig = int(input("numero de cigarros: "))
an =int(input("anos fumando: "))
print(vida(cig, an))