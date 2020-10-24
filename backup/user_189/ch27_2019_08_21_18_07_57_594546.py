ncigar=int(input("quantos cigarros vc fuma por dia?: "))
timecigar=int(input("há quantos anos vc fuma?: "))
def lost_timelife(ncigar, timecigar):
    tmlostmin=(ncigar*10)*timecigar*365
    tmlostday=tmlostmin/1440
    tmlostyear=tmlostmin/525600

    return [tmlostmin, tmlostday, tmlostyear]
a=lost_timelife(ncigar, timecigar)

print("tempo de vida perdido: {0:.2f} minutos ou {1:.2f} dias ou {2:.2f} anos".format(a[0],a[1],a[2]))
