a = float(input('Digite a distância que deseja percorrer: '))
if a<200:
    print(a * 0.50)
else:
    print((200 * 0.50) + ((a-200)*0.45))