a=int(input('Km?'))
c=a*0.5
if a<=200:
    c=a*0.5
    print ('R${:.2f}'.format(c))
if a>=200:
    x=0.45*(a-200)+c
    print ('R${:.2f}'.format(x))