"""Usuarios:
1. Diseña un programa que permite guardar el nombre de usuario y contraseña de
hasta 10 usuarios diferentes. Si el usuario ya existe en el sistema, puede hacer
login tras incluir un usuario y contraseña válidas hasta un máximo de tres
intentos, momento en el que se bloquea su cuenta.
Si el usuario no existe, puede crear una cuenta siempre que haya espacio
(máximo 10), para lo que se le pedirá usuario y contraseña, así como la
confirmación de ésta última.
El menú de este programa permitirá identificarse y crear cuentas nuevas, así
como mostrar todos los nombres de usuario existentes sin sus contraseñas."""

baseUsuarios={"MIKI":"123123"}

def menu(opcion):
    pantalla="""
    1. Crear Usuario
    2. Logear en el sistema
    3. Mostrar Menu
    4. Mostrar Base de datos
    5. Salir
    """
    salida=""
    if opcion==1:
        print("Vamos a crear un usuario")
        salida=1
    elif opcion==2:
        print("Vamos a logear")
        salida=2
    elif opcion==3:
        print(pantalla)
    elif opcion==4:
        print("Mostrando base de datos")
        salida=4
    elif opcion==5:
        print("Cerrando programa")
        quit()
    else:
        print("Esa opcion no existe, introduce 3 para ver menu")
    return salida

def crearUsuario(user, password, repeatpass,baseUsuarios=baseUsuarios):
    valid=0
    restrictions="1234567890!·$%&/()=?¿Çç*+^`¨´´';,.-_}{][|@#\ºª¬ "
    if len(baseUsuarios)==10:
        valid=0
        print("La base de datos esta llena")
    elif user[0] in restrictions:
        valid=0
        print("El nombre de usuario debe empezar por un caracter alfabetico")
    elif len(password)< 6:
        valid=0
        print("La contraseña tiene que tener almenos 6 caracteres")
    elif password!=repeatpass:
        valid=0
        print("La contraseña no coincide")
    else:
        valid=baseUsuarios[user]=password

    
    return valid

def logear(usuario,password,base_datos=baseUsuarios):
    valido=True
    fallos=0
    if base_datos.get(usuario)=="Bloqueado":
        print("El usuario esta bloqueado, contacte con su administrador")
    elif usuario in base_datos and base_datos.get(usuario)!="Bloqueado":
        while password!=base_datos[usuario] and fallos <=3:
            fallos+=1
            password=int(input(f"Introduce de nuevo la contraseña (Intento {fallos}/3):"))
            if fallos >=3:
                print("El usuario ha quedado bloqueado")
                base_datos[usuario]="Bloqueado"
                valido=False
            if valido==False:
                return valido
        if base_datos[usuario]==password:
            print("Accediendo al sistema")
            valido=True
                
    else:
        print("El usuario no existe")
        valido=False
    return valido

def main():
    try:
        opcion=0
        while opcion!=5:
            opcion=int(input("Introduce opcion: "))
            if opcion==1 and len(baseUsuarios) <10:
                menu(1)
                user=input("Introduzca nombre de usuario deseado: ")
                password=input("Introduzca contraseña: ")
                repeatpass=input("Repita contraseña: ")
                if user in baseUsuarios:
                    print("El usuario ya existe en el sistema")
                    menu(2)
                else:
                    while crearUsuario(user,password,repeatpass)==0:
                        user=input("Introduzca nombre de usuario deseado: ")
                        password=input("Introduzca contraseña: ")
                        repeatpass=input("Repita contraseña: ")
                    

            elif opcion==2:
                menu(2)
                logear(usuario=input("Introduce usuario: "), password=input("Introduce contraseña: "))
            elif opcion==4:
                keys=""
                menu(4)
                for i in baseUsuarios.keys():
                    keys+=i+" "
                print(keys)
            else: menu(opcion)
    except ValueError:
        print("Introduce 3 para ver menu")
        main()

if __name__=="__main__":
    
    print(menu(3))
    main()
        

    
#CALCULO
"""1. Write a Python program to calculate the sum of digits of a number.
"""

def sumarDigitos(numero):
    numero=str(numero)
    total=0
    for n in numero:
        total=total+int(n)

    return total

assert(sumarDigitos(2)==2)
assert(sumarDigitos(25)==7)

"""2. Write a Python program to compute the greatest common divisor (GCD) of two
positive integers"""

def maximo_comun_divisor(numero1,numero2):
    divisores1=[]
    divisores2=[]
    comunes=[]
    for div1 in range(1,numero1+1):
        if numero1%div1==0:
            divisores1.append(div1)
    for div2 in range(1,numero2+1):
        if numero2%div2==0:
            divisores2.append(div2)

    for i in divisores1:
        if i in divisores2:
            comunes.append(i)

    return comunes[-1]


assert(maximo_comun_divisor(10,5)==5)

"""3. Write a Python program to get the least common multiple (LCM) of two positive
integers.
"""

def minimo_comun_multiplo(numero1,numero2):
    mcm=(numero1*numero2)/maximo_comun_divisor(numero1,numero2)
    return mcm

assert(minimo_comun_multiplo(12,8)==24)
assert(minimo_comun_multiplo(4,2)==4)

"""4. Write a Python program that accepts two integers (n and i) and computes the value
of n+nn+nnn+...."""

def sumar_patron(numero1, numero2):
    suma=""
    for i in range(1,numero2+1):
        suma+=str(i*numero1)
    return int(suma)
   
assert(sumar_patron(2,3)==246)
assert(sumar_patron(1,5)==12345)

"""5. Queremos crear un programa que trabaje con fracciones de la forma a/b. Para
representar una fracción vamos a utilizar dos enteros: numerador y denominador,
creando las siguientes funciones para trabajar con ellas:
i. leer_fracción: La tarea de esta función es leer por teclado el numerador y el
denominador y la devuelve simplificada (Por ejemplo, si recibe 16/6 ⇒ 8/3)
ii. escribir_fracción: muestra por pantalla la fracción; si el denominador es 1, se
muestra sólo el numerador.
iii. calcular_mcd: Esta función recibe dos números y devuelve su máximo común
divisor.
iv. simplificar_fracción: simplifica una fracción. Para ello hay que dividir el
numerador y denominador por su MCD.
v. sumar_fracciones: recibe dos funciones n1/d1 y n2/d2 y calcula su suma. La
suma de dos fracciones es otra fracción cuyo numerador n=n1*d2+d1*n2 y
denominador d=d1*d2, simplificando la fracción resultado.
vi. restar_fracciones: resta dos fracciones, siendo el numerador de la resta
n=n1*d2-d1*n2 y el denominador d=d1*d2, simplificando el resultado.
vii. multiplicar_fracciones: recibe dos fracciones y calcula su producto, siendo el
numerador del producto n=n1*n2 y el denominador d=d1*d2 (simplificando).
viii. dividir_fracciones: calcula el cociente de dos fracciones, siendo el numerador
n=n1*d2 y denominador d=d1*n2 (simplificando el resultado).
"""

def leer_fraccion(numerador,denominador):
    n=0
    if numerador>denominador:
        while n < numerador:
            n+=1
            if numerador%n==0 and denominador%n==0:
                numerador=numerador//n
                denominador=denominador//n
    return numerador,denominador


assert(leer_fraccion(16,6)==(8,3))

def escribir_fraccion(numerador,denominador):
    fraccion=0
    if denominador==1:
        print(numerador)
    else:
        print(f"{numerador}/{denominador}")

escribir_fraccion(2,5)


def simplificar_fraccion(numerador,denominador):
    numeradorsimp=numerador//maximo_comun_divisor(numerador,denominador)
    denominadorsimp=denominador//maximo_comun_divisor(numerador,denominador)
    return numeradorsimp, denominadorsimp

assert(simplificar_fraccion(8,4)==(2,1))

def sumar_fraccion(numerador1,denominador1,numerador2,denominador2):
    numerador=(numerador1*denominador2)+(denominador1*numerador2)
    denominador=denominador1*denominador2
    return simplificar_fraccion(numerador,denominador)

def restar_fraccion(numerador1,denominador1,numerador2,denominador2):
    numerador=(numerador1*denominador2)-(denominador1*numerador2)
    denominador=denominador1*denominador2
    return simplificar_fraccion(numerador,denominador)   

def multiplicar_fraccion(numerador1,denominador1,numerador2,denominador2):
    numerador=numerador1*denominador1
    denominador=denominador1*denominador2
    return simplificar_fraccion(numerador,denominador)

def dividir_fraccion(numerador1,denominador1,numerador2,denominador2):
    numerador=numerador1*denominador2
    denominador=numerador2*denominador1
    return simplificar_fraccion(numerador,denominador)

"""6. Crear un programa que utilizando las funciones anteriores muestre el siguiente
menú:
a. Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el
resultado.
b. Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la
resta.
c. Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el
producto.
d. Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la
cociente.
e. Salir"""

opcion=""
pantalla="""
a. Sumar dos fracciones.
b. Restar dos pracciones.
c. Multiplicar dos fracciones.
d. Dividir dos fracciones.
e. Salir"""
while opcion != "e":
    print(pantalla)

    opcion=input("Introduzca una opcion: ").lower()

    if opcion=="a":
        print(sumar_fraccion(int(input("Introduzca numerador1: ")),int(input("Introduzca denominador1: ")),int(input("Introduzca numerador2: ")),int(input("Introduzca denominador2: "))))
    elif opcion=="b":
        print(restar_fraccion(int(input("Introduzca numerador1: ")),int(input("Introduzca denominador1: ")),int(input("Introduzca numerador2: ")),int(input("Introduzca denominador2: "))))
    elif opcion=="c":
        print(multiplicar_fraccion(int(input("Introduzca numerador1: ")),int(input("Introduzca denominador1: ")),int(input("Introduzca numerador2: ")),int(input("Introduzca denominador2: "))))
    elif opcion=="d":
        print(dividir_fraccion(int(input("Introduzca numerador1: ")),int(input("Introduzca denominador1: ")),int(input("Introduzca numerador2: ")),int(input("Introduzca denominador2: "))))
    else:
        print("\nIntroduzca una opcion del menu")

"""Figuras:
1. Define una función que calcule el área de un círculo dado su radio.
2. Defina una función que dado el radio de un círculo devuelva su longitud.
3. Función tal que dadas las coordenadas de dos puntos en el plano devuelve su
distancia euclídea. Un punto en el plano tiene dos coordenadas (abscisa y
ordenada), por lo tanto, la entrada a esta función son cuatro valores reales.
4. Función tal que dadas las coordenadas de un triángulo en el plano, nos devuelve
su perímetro.
5. Haciendo uso de la función anterior diseña otra que calcule su área.
"""

def calcular_area_circulo(radio):
    PI=3.1416
    return f"{PI*(radio**2):.2f}"

def longitud_circulo(radio):
    PI=3.1416
    return f"{PI*(radio*2):.2f}"

def distancia_euclidea(x1,y1,x2,y2):
    return f"{(((x2-x1)**2)+((y2-y1)**2))**0.5:.2f}"

def perimetro_triangulo(x1,y1,x2,y2,x3,y3):
    return f"{((((x2-x1)**2)+((y2-y1)**2))**0.5)+((((x3-x2)**2)+((y3-y2)**2))**0.5)+((((x3-x1)**2)+((y3-y1)**2))**0.5):.2f}"


def area_triangulo(x1,y1,x2,y2,x3,y3):
    return f"{(((((x2-x1)**2)+((y2-y1)**2))**0.5)+((((x3-x2)**2)+((y3-y2)**2))**0.5)+((((x3-x1)**2)+((y3-y1)**2))**0.5))*0.5:.2f}"


"""Fechas:
1. Función que dado un instante (horas, minutos y segundos) devuelva el número
de segundos transcurridos desde el inicio de un día hasta ese instante.
2. Crea una función que devuelva la diferencia en segundos entre dos instantes de
tiempo del mismo día. Recibirá como parámetros seis valores, hora, minuto y
segundo de cada uno de los instantes.
3. Write a Python program to convert seconds to day, hour, minutes and seconds.
4. Write a Python program to calculate the number of days between two dates.
5. Write a Python program to print the calendar of a given month and year. If you
feel confident enough, extend it to cover a complete year (See annex).
"""

def calcular_segundos(horas,minutos,segundos):
    if horas > 24 or minutos > 60 or segundos>60:
        print("Introduce horario valido")
    else:
        return ((horas*60)*60)+(minutos*60)+segundos

assert(calcular_segundos(2,0,0)==7200)

def diferencia_dia(horas1,minutos1,segundos1,horas2,minutos2,segundos2):
    instante1=calcular_segundos(horas1,minutos1,segundos1)
    instante2=calcular_segundos(horas2,minutos2,segundos2)
    return instante1-instante2

assert(diferencia_dia(12,12,12,12,12,12)==0)
assert(diferencia_dia(13,12,12,12,12,12)==3600)

def converetidor_horario(segundos):

    dias=int((segundos//60)//60)//24
    horas=int((segundos//60)//60)%24
    minutos=int(segundos//60)%60
    segundos=int(segundos)%120

    return dias, horas, minutos, segundos
assert(converetidor_horario(118560)==(1,8,56,0))

def bisiesto(year):
    if (year %4==0) and (year%100!=0 or year%400==0):
        return True
    else:
        return False

def dias_pasados(dia,mes,year): #Ejercicio realizado en un boletin anterior
    try:
        meses=1
        meslargo=[3,5,7,8,10,12]
        totaldias=0
        totaltranscurrido=0
        if (dia >31 or dia < 1) or (mes>12 or mes<1) or (dia>29 and mes==2) or (dia==29 and bisiesto(year)==False):
            print("Introduzca una fecha correcta porfavor")
            totaltranscurrido=False
        else:

            if mes==1:
                totaltranscurrido=dia
            elif bisiesto(year)==True:
                while meses < mes:
                    if meses==2:
                        totaldias+=29
                    elif meses in meslargo:
                        totaldias+=31
                    else:
                        totaldias+=30
                    meses+=1
                totaltranscurrido=(totaldias)+(dia)+1
            else:
                while meses < mes:
                    if meses==2:
                        totaldias+=28
                    elif meses in meslargo:
                        totaldias+=31
                    else:
                        totaldias+=30
                    meses+=1
                totaltranscurrido=(totaldias)+(dia)+1

    except:
        print("Introduzca valores en formato dd-mm-yyyy")
    return totaltranscurrido

def dias_entre_fechas(dia1,mes1,year1,dia2,mes2,year2):
    years=0
    if year1!=year2:
        years=abs(year1-year2)*365
    return abs(dias_pasados(dia1,mes1,year1)-dias_pasados(dia2,mes2,year2))+years

assert(dias_entre_fechas(24,2,2002,20,2,2002)==4)

def getDayOfWeek(day,month,year):
    daysmonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    dayinweek={0:"Domingo",1:"Lunes",2:"Martes",3:"Miercoles",4:"Jueves",5:"Viernes",6:"Sabado"}
    try:
        if month<1 or year<1:
            print("Introduzca valores validos")
        else:
            a = (14 - month)//12
            y = year - a
            m = month + 12 * a - 2
            d= int(((day + y + y//4 - y//100 + y//400 + (31*m)//12)%7))
            d=dayinweek[d]
    except:
        print("Valores invalidos")
    return d

def calendar(month,year):
    calendario=""
    day=getDayOfWeek(1,month,year)
    if day=="Lunes" and month==2 and bisiesto(year)==False:
        calendario="""
        L    M    X    J    V    S    D
        1    2    3    4    5    6    7
        8    9    10   11   12   13   14
        15   16   17   18   19   20   21
        22   23   24   25   26   27   28
        """        
    elif day=="Martes" and month==2 and bisiesto(year)==False:
        calendario="""
        L    M    X    J    V    S    D
             1    2    3    4    5    6
        7    8    9    10   11   12   13
        14   15   16   17   18   19   20
        21   22   23   24   25   26   27
        28 
        """
    elif day=="Miercoles" and month==2 and bisiesto(year)==False:
        calendario="""
        L    M    X    J    V    S    D
                  1    2    3    4    5
        6    7    8    9    10   11   12
        13   14   15   16   17   18   19
        20   21   22   23   24   25   26
        27   28 
        """
    elif day=="Jueves" and month==2 and bisiesto(year)==False:
        calendario="""
        L    M    X    J    V    S    D
                       1    2    3    4
        5    6    7    8    9    10   11
        12   13   14   15   16   17   18
        19   20   21   22   23   24   25
        26   27   28     
        """     
    elif day=="Viernes" and month==2 and bisiesto(year)==False:
        calendario="""
        L    M    X    J    V    S    D
                            1    2    3
        4    5    6    7    8    9    10
        11   12   13   14   15   16   17
        18   19   20   21   22   23   24
        25   26   27   28 
        """             
    elif day=='Sabado' and month==2 and bisiesto(year)==False:
        calendario="""
        L    M    X    J    V    S    D
                                 1    2
        3    4    5    6    7    8    9
        10   11   12   13   14   15   16
        17   18   19   20   21   22   23
        24   25   26   27   28 
     
        """
    elif day=="Domingo" and month==2 and bisiesto(year)==False:
        calendario="""
        L    M    X    J    V    S    D
                                      1
        2    3    4    5    6    7    8
        9    10   11   12   13   14   15
        16   17   18   19   20   21   22
        23   24   25   26   27   28   
        """
    elif day=="Lunes" and month==2 and bisiesto(year):
        calendario="""
        L    M    X    J    V    S    D
        1    2    3    4    5    6    7
        8    9    10   11   12   13   14
        15   16   17   18   19   20   21
        22   23   24   25   26   27   28
        29
        """        
    elif day=="Martes" and month==2 and bisiesto(year):
        calendario="""
        L    M    X    J    V    S    D
             1    2    3    4    5    6
        7    8    9    10   11   12   13
        14   15   16   17   18   19   20
        21   22   23   24   25   26   27
        28   29
        """
    elif day=="Miercoles" and month==2 and bisiesto(year):
        calendario="""
        L    M    X    J    V    S    D
                  1    2    3    4    5
        6    7    8    9    10   11   12
        13   14   15   16   17   18   19
        20   21   22   23   24   25   26
        27   28   29
        """
    elif day=="Jueves" and month==2 and bisiesto(year):
        calendario="""
        L    M    X    J    V    S    D
                       1    2    3    4
        5    6    7    8    9    10   11
        12   13   14   15   16   17   18
        19   20   21   22   23   24   25
        26   27   28   29  
        """     
    elif day=="Viernes" and month==2 and bisiesto(year):
        calendario="""
        L    M    X    J    V    S    D
                            1    2    3
        4    5    6    7    8    9    10
        11   12   13   14   15   16   17
        18   19   20   21   22   23   24
        25   26   27   28   29
        """             
    elif day=='Sabado' and month==2 and bisiesto(year):
        calendario="""
        L    M    X    J    V    S    D
                                 1    2
        3    4    5    6    7    8    9
        10   11   12   13   14   15   16
        17   18   19   20   21   22   23
        24   25   26   27   28   29
     
        """
    elif day=="Domingo" and month==2 and bisiesto(year):
        calendario="""
        L    M    X    J    V    S    D
                                      1
        2    3    4    5    6    7    8
        9    10   11   12   13   14   15
        16   17   18   19   20   21   22
        23   24   25   26   27   28   29  
        """
    elif day=="Lunes" and (str(month) in "13578" or month == 10 or month==12):
        calendario="""
        L    M    X    J    V    S    D
        1    2    3    4    5    6    7
        8    9    10   11   12   13   14
        15   16   17   18   19   20   21
        22   23   24   25   26   27   28
        29   30   31
        """
    elif day=="Martes" and (str(month) in "13578" or month == 10 or month==12):
        calendario="""
        L    M    X    J    V    S    D
             1    2    3    4    5    6
        7    8    9    10   11   12   13
        14   15   16   17   18   19   20
        21   22   23   24   25   26   27
        28   29   30   31
        """
    elif day=="Miercoles" and (str(month) in "13578" or month == 10 or month==12):
        calendario="""
        L    M    X    J    V    S    D
                  1    2    3    4    5
        6    7    8    9    10   11   12
        13   14   15   16   17   18   19
        20   21   22   23   24   25   26
        27   28   29   30   31
        """
    elif day=="Jueves" and (str(month) in "13578" or month == 10 or month==12):
        calendario="""
        L    M    X    J    V    S    D
                       1    2    3    4
        5    6    7    8    9    10   11
        12   13   14   15   16   17   18
        19   20   21   22   23   24   25
        26   27   28   29   30   31    
        """     
    elif day=="Viernes" and (str(month) in "13578" or month == 10 or month==12):
        calendario="""
        L    M    X    J    V    S    D
                            1    2    3
        4    5    6    7    8    9    10
        11   12   13   14   15   16   17
        18   19   20   21   22   23   24
        25   26   27   28   29   30   31
        """             
    elif day=='Sabado' and (str(month) in "13578" or month == 10 or month==12):
        calendario="""
        L    M    X    J    V    S    D
                                 1    2
        3    4    5    6    7    8    9
        10   11   12   13   14   15   16
        17   18   19   20   21   22   23
        24   25   26   27   28   29   30
        31
        """
    elif day=="Domingo" and (str(month) in "13578" or month == 10 or month==12):
        calendario="""
        L    M    X    J    V    S    D
                                      1
        2    3    4    5    6    7    8
        9    10   11   12   13   14   15
        16   17   18   19   20   21   22
        23   24   25   26   27   28   29
        30   31
        """             
    elif day=="Lunes":
        calendario="""
        L    M    X    J    V    S    D
        1    2    3    4    5    6    7
        8    9    10   11   12   13   14
        15   16   17   18   19   20   21
        22   23   24   25   26   27   28
        29   30
        """
    elif day=="Martes":
        calendario="""
        L    M    X    J    V    S    D
             1    2    3    4    5    6
        7    8    9    10   11   12   13
        14   15   16   17   18   19   20
        21   22   23   24   25   26   27
        28   29   30
        """
    elif day=="Miercoles":
        calendario="""
        L    M    X    J    V    S    D
                  1    2    3    4    5
        6    7    8    9    10   11   12
        13   14   15   16   17   18   19
        20   21   22   23   24   25   26
        27   28   29   30
        """
    elif day=="Jueves":
        calendario="""
        L    M    X    J    V    S    D
                       1    2    3    4
        5    6    7    8    9    10   11
        12   13   14   15   16   17   18
        19   20   21   22   23   24   25
        26   27   28   29   30    
        """     
    elif day=="Viernes":
        calendario="""
        L    M    X    J    V    S    D
                            1    2    3
        4    5    6    7    8    9    10
        11   12   13   14   15   16   17
        18   19   20   21   22   23   24
        25   26   27   28   29   30
        """             
    elif day=='Sabado':
        calendario="""
        L    M    X    J    V    S    D
                                 1    2
        3    4    5    6    7    8    9
        10   11   12   13   14   15   16
        17   18   19   20   21   22   23
        24   25   26   27   28   29   30
     
        """
    elif day=="Domingo":
        calendario="""
        L    M    X    J    V    S    D
                                      1
        2    3    4    5    6    7    8
        9    10   11   12   13   14   15
        16   17   18   19   20   21   22
        23   24   25   26   27   28   29
        30
        """             
    return calendario        


print(calendar(3,2001))
