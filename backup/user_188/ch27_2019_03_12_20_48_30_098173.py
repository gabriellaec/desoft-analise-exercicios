def vida(num_cig, anos):
    mes = anos * 12
    semana = mes * 4
    dias = semana * 7
    horas = 24*dias
    minutos = 60*horas
    tempo_min = num_cig * minutos * 10
    tempo_horas = tempo_min / 60
    tempo_dias = tempo_horas / 24
    return tempo_dias

cig = int(input("numero de cigarros: "))
an =int(input("anos fumando: "))
print(vida(cig, an))