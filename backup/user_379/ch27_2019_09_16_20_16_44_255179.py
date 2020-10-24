def funcao(a,b):
	cigarros_em_um_ano=(365*b)
	cigarros_durante_a_vida=(cigarros_em_um_ano*a)
    if a!=0 and b!=0:
        tempo_de_vida_perdido=(cigarros_durante_a_vida*60*1440)/(10*cigarros_durante_a_vida)
		return tempo_de_vida_perdido
    else:
        tempo_de_vida_perdido==0
a=int(input("digite o tempo que você fuma em anos"))
b=int(input("digite quantos por dia"))
print(funcao(a,b))