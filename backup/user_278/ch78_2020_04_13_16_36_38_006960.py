import math 
atletas = {}
      
while True:
    nome = input("qual o nome do atleta?: ")
    if nome == "sair":
        break
    else:
        atletas [nome] = int(input("qual a aceleração desse atleta?: "))

for k,v in atletas.items():
    atletas [k] = math.sqrt(200/v)    

t = list (atletas.values())
atleta = list (atletas.keys())       
                
print (f"O vencedor é {atleta[t.index(min(t))]} com tempo de conclusão de {min(t)} s")