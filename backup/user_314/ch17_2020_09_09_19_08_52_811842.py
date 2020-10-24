def eh_bissexto (x):
    if (x%4==0):
        if(x%100!=0):
            print("True")
         else:
            print("False")
    else:
        if(x%4!=0):
            if(x%400==0):
                print("True")
             else:
                print("False")