def eh_bissexto (x):
    if (x%400==0):
        print("True")
    else:
    
        if (x%4==0) and (x%100!=0):
            print("True")
        else:
            print("False")
  