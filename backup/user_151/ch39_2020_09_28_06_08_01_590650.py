i = 1
j = 1
k = 1 
x = 0
while i < 1001:
	
	while j != 1:
		
	
		if j % 2 == 0:
			j = j/2
			k = k + 1
			
		else:
			j = 3*j + 1
			k = k + 1
			
	if k > x:
		x = k
		y = i
	k = 1
	
	


	i = i + 1
	j = i
	

print(y)