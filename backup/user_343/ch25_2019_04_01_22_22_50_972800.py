a=int(input('Km?'))
if a<201:
    c=a*0.5
    print ('R${:.2f}'.format(c))
else:
    x=0.45*(a-200)+a*0.5
    print ('R${:.2f}'.format(x))