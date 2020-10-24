import math
def eh_bissexto(a):
    if a%4==0 or a==1:
        if len(str(a))>3 and a%400!=0:
            print(False)
        else:
            print(True)
    else:
    	print(False)