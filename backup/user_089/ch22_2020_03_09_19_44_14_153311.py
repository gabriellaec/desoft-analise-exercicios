D= int(input("quantos cigarros voce fuma por dia?: "))
A= int(input("Há quantos anos voce fuma?: "))

print( int(((D*10)/1440) + (365*((D*10)/1440))) )