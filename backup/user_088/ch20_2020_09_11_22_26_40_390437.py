distância = float(input("Digite a distância a percorrer: "))
if (distância <= 200):
    total = 0.5 * distância
    print("%.1f" %total)
else:
    total = 0.45 * (distância)
    print("%.1f" %total)