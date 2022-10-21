def area_cuadrado():#funcion del area del perimetro
    lado=int(input('Dime el valor del lado en cm: '))
    solucion=lado*4
    print('El perimetro = {} cm'.format(solucion))

def area_rectangulo():#funcion del area del perimetro
    a=int(input('Dime el valor del lado en cm: '))
    b=int(input('Dime el valor del lado en cm: '))
    solucion=a*b
    print('El perimetro = {} cm'.format(solucion))

def area_paralelogramo():#funcion del area del perimetro
    b=int(input('Dime el valor del lado en cm: '))
    h=int(input('Dime el valor del altura en cm: '))
    solucion=h*b
    print('El perimetro = {} cm'.format(solucion))

def area_rombo():#funcion del area del perimetro
    a=int(input('Dime el valor de la punta en cm: '))
    b=int(input('Dime el valor de la punta en cm: '))
    c=int(input('Dime el valor de la punta en cm: '))
    d=int(input('Dime el valor de la punta en cm: '))
    solucion=(a*c)*(b*d)/2
    print('El perimetro = {} cm'.format(solucion))

def area_Trapecio():#funcion del area del perimetro
    a=int(input('Dime el valor del lado en cm: '))
    b=int(input('Dime el valor del lado en cm: '))
    h=int(input('Dime el valor de la altura en cm: '))
    solucion= ((a*b)/2)*h
    print('El perimetro = {} cm'.format(solucion))

def area_Triangulo():#funcion del area del perimetro
    a=int(input('Dime el valor del lado en cm: '))
    solucion= (a*1.73)/4
    print('El perimetro = {} cm'.format(solucion))

def area_circulo():#funcion del area del circulo
    radio=int(input('Dime cuantos cm mide el radio: '))
    solucion=3,1416*radio**2
    print('El Área del circulo = {} cm2'.format(solucion))
 
def menu():#solo muestra el menú para elegir
    print('''
1_ Area de un cuadrado
2_ area de un rectangulo
3_area_circulo
4_area_paralelogramo
5_area_rombo
6_area_Trapecio
7_area_Triangulo
8_
9_
'''
)
menu()
elegir=int(input('Elige : ' ))#pregunta almacenada en la variable que te lleva a las funciones
if elegir==1:
    area_cuadrado()
elif elegir==2:
    area_rectangulo()
elif elegir==3:
    area_circulo()
elif elegir==4:
    area_paralelogramo()
elif elegir==5:
    area_rombo()
elif elegir==6:
	area_Trapecio()
elif elegir==7:
	area_Triangulo()
else:
    print('Sólo puedes elegir 1 o 2')
    elegir=int(input('Elige 1 o 2: '))