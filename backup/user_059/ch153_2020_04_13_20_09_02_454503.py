def agrupa_por_idade(dici):
    idade = list(dici.values()) 
    nome = list(dici.keys())
    lcri = []
    lado = []
    ladu = []
    lido = []
    for i in range(len(dici)):
        if idade[i] <= 11:
            lcri.append(nome[i])
        elif 12 <= idade[i] <= 17:
            lado.append(nome[i])
        elif 18 <= idade[i] <= 59:
            ladu.append(nome[i])
        else:
            lido.append(nome[i])            
    novod = {'criança' : lcri, 'adolescente' : lado, 'adulto' : ladu, 'idoso' : lido}
    return novod