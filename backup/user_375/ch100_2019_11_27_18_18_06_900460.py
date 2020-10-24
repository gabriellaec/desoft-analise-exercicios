login_new = ""

while login_new != "fim":
	login_new = input("Qual o seu login? ")
	if login_new != "fim":
		logins.append(login_disponivel(login_new, logins))

for login in logins:
	print(login)