distância=int(input("Digite a distância que você deseja percorrer em Km: ")
if distância<=200:
              total=distância*0.5
else:
              total=(distância-200)*0.45 + 100
print("O seu resultado é {0:.2f}". format (total))