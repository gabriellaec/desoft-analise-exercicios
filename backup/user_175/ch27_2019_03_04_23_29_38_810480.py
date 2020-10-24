num_cigarros = int(input())
tempo_fumo = int(input())
tempo_perdido = (((365*tempo_fumo)*(num_cigarros)*10)/1440)
print(tempo_perdido)