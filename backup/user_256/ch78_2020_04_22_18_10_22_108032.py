nome = input("digite o nome: ")
while nome != 'sair':
    aceleração = input("Digite a aceleração: ")

def calcula_tempo(atletas_para_aceleração):
    
    atletas_para_tempodeprova = {}
    for atletas, aceleração in atletas_para_aceleração.items():
        tempo = (200/aceleração)**0.5 
        atletas_para_tempodeprova[atletas] = tempo
    return atletas_para_tempodeprova

print ('O vencedor é {0} com tempo de conclusão de {1} s'.format(atletas, tempo))
