v=int(input('quantos km/h? '))
if v <= 80:
    print ('Não foi multado')
else:
    t=(v-80)*5
    print ("%.2f"%t)