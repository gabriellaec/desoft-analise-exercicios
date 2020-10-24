ncigar=int(input("quantos cigarros vc fuma por dia?: "))
timecigar=int(input("há quantos anos vc fuma?: "))
def lost_timelife(ncigar, timecigar):
    tmlostmin=(ncigar*10)*timecigar*365
    tmlostday=tmlostmin/1440
    #tmlostyear=tmlostmin/525600

    return tmlostday


