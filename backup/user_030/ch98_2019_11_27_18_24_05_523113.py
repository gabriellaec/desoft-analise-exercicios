def total_do_semestre_por_bairro(bairros):

    gastos_por_semestre = {}
    for bairro, gastos in bairros.items():
        soma_gastos = 0;

        indice = 0;
        for gasto in gastos:
            if(indice < 6):
                soma_gastos = soma_gastos+gasto
            indice = indice+1

        gastos_por_semestre[bairro] = soma_gastos

    return gastos_por_semestre



bairros = {
    'Vila Olimpia': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Brooklin': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Itaim': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
}

gastos_por_semestre = total_do_semestre_por_bairro(bairros)

bairro_maior_custo=""
maior_custo = 0;
for bairro, gastos in gastos_por_semestre.items():
    if(gastos > maior_custo):
        bairro_maior_custo = bairro
        maior_custo = gastos

print("Bairro com maior custo é", bairro_maior_custo, "com gasto no semestre", float("{0:.2f}".format(maior_custo)))