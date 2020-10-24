import math 
atletas = {}
nome = input("qual o nome do atleta?: ")
      
while nome != "sair":
    atletas [nome] = ace = int(input("qual a aceleração desse atleta?: ")
    nome = input("qual o nome do atleta?: ")

for k,v in atletas.items():
    atletas [k] = math.sqrt(200/v)    

t = list (atletas.values())
atleta = list (atletas.keys())       
                
print (f"O vencedor é {atleta} com tempo de conclusão de {t} s")