import math
def eh_bissexto(a):
    if a%4==0:
        if len(a)>3 and a%400!=0:
            print(False)
        else:
            print(True)
    else:
    	print(False)