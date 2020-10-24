bairros = {
    'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
}

def total_do_semestre_por_bairro(bairros):
	semestre = {}

	for bairro, meses in bairros.items():
		valor = 0.0

		for mes in meses:
			if meses.index(mes) > 5:
				valor += mes
		
		semestre[bairro] = valor

	return semestre

semestre = total_do_semestre_por_bairro(bairros)

def bairro_mais_custoso(semestre):
	valor_maior = 0.0

	for bairro, valor in semestre.items():
		if valor > valor_maior:
			valor_maior = valor
			bairro_maior = bairro
	
	return bairro_maior