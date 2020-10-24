a= float(input("distância desejada :"))
    if a <= 200:
		y= 0.50 * a
    else:
        y= 0.45 * (a-200) + 100
        print y
		
    
    