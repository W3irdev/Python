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

"""if __name__=="__main__":
    
    print(menu(3))
    main()"""
        

    
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