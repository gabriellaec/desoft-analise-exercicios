cigarros_dia = int(input())
anos = int(input())
dias = anos*365
cigarros = cigarros_dia * dias
tempo_minutos = cigarros *10
tempo_dias = tempo_minutos / (24 * 60)
print(tempo_dias)