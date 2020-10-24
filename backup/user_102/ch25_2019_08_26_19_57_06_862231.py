km = float(input())
if km <= 200:
    return(km*0.50)
elif km > 200:
    return((200*0.50) + ((km-200)*0.45))