n = int(input("ingrese la nota del estudiante  \n "))

if(n == 0):
	print("el nuemro ingresado "+ str(n) +" es nulo")

if(n >= 30):
	print("el estudiante saco la nota"+ str(n) +" asi que aprobo")
else:
	print("el estudiante saco la nota"+ str(n) +" asi que No aprobo")