distância = float(input("Digite uma distância"))

if distância < 200:
    preço = distância * 0.5

else:
    preço = 199 * 0.5 + (distância - 200) * 0.45
 
print(preço)