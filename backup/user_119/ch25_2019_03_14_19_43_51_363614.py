km=int(input("Quantos km? ")
def preco(km):
       if km<=200:
          return km*0.5
       else:
          return 100+(km-200)*0.45
print ('{0:.2f}'.format(preco(km))
