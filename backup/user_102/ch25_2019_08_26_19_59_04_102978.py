km = float(input())
if km <= 200:
    print("{0:.2f}".format(km*0.50))
elif km > 200:
    print("{0:.2f}".format((200*0.50) + ((km-200)*0.45)))