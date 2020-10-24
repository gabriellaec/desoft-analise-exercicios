a=int(input("quantos km"))
if a<=200:
    return(a*0.5)
else:
    return((200*0.5)+((a-200)*0.45))