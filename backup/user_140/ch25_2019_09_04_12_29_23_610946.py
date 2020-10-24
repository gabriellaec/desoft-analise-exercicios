km=int(input())
if km <= 200:
    preco_passagem=km*0.5
else:
    preco_passagem=((200*0.5)+((km-200)*0.45))
print(round(preco_passagem,2))