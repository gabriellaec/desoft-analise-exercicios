a=int(input("quantos km"))
if a<=200:
    print(a*0.5)
else:
    return((200*0.5)+((a-200)*0.45))