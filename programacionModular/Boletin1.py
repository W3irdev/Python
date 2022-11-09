def conocer(comparador,lista):
    mayor=0
    menor=1001
    suma=0
    if comparador=="MAYOR":
        for x in range(len(lista)):
            if lista[x] > mayor:
                mayor=lista[x]
        return mayor
    elif comparador=="MENOR":
        for x in range(len(lista)):
            if lista[x] < menor:
                menor=lista[x]
        return menor
    elif comparador=="SUMA":
        for x in (lista):
            suma+=x
        return suma
from random import randint

"""1. Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000)"""

# CONOCER MAYOR
numeros=[]

for i in range(100):
    numeros.append(randint(0,1000))


def conocer(comparador):
    mayor=0
    suma=0
    menor=1001
    if comparador=="MAYOR":
        for x in range(len(numeros)):
            if numeros[x] > mayor:
                mayor=numeros[x]
        resultado=mayor
    elif comparador=="MENOR":
        for x in range(len(numeros)):
            if numeros[x] < menor:
                menor=numeros[x]
        resultado=menor
    elif comparador=="SUMA":
        for x in (numeros):
            suma+=x
        resultado=suma
    return resultado

print(conocer("MAYOR"))

#CONOCER MENOR

print(conocer("MENOR"))

#SUMA DE TODOS LOS NUMEROS

print(conocer("SUMA"))

#OBTENER LA MEDIA

print(conocer("SUMA")/len(numeros))

#SUSTITUIR VALOR DE UN ELEMENTO POR OTRO NUMERO INTRODUCIDO POR TECLADO
print(numeros)
valor=int(input("¿Que valor desea sustituir? "))
sustituto=int(input("¿Que numero desea introducir en la lista? "))

def sustituir(valor,sustituto,lista):
    for i in range(len(lista)):
        if lista[i]==valor:
            lista[i]=sustituto
sustituir(valor,sustituto,numeros)
#MOSTRAR TODOS LOS NUMEROS

print(numeros)

"""2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.).
"""

numeros2=[]
for i in range(10):
    numeros2.append(i)

numeros2=[]
for i in range(10):
    numeros2.append(i)

def desplazar(direccion,posicion):
    posicion=posicion%10
    desplazado=""
    if direccion=="D":
        for x in numeros2:
            d=x-posicion
            direccion=d
            if x+1==len(numeros2):
                desplazado+=str(numeros2[direccion])
            else:
                desplazado+=str(numeros2[direccion])+", " 
    elif direccion=="I":
        for x in numeros2:
            i=x-(10-posicion)
            direccion=i
            if x+1==len(numeros2):
                desplazado+=str(numeros2[direccion])
            else:
                desplazado+=str(numeros2[direccion])+", " 
        
    return desplazado
    
print(desplazar("I",0))


"""3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo"""

day=0
month=0
year=0
while day>-1:
    day=0
    while day==0 or day>31:
        day=int(input("Introduzca dia mayor 0 y menor de 31: "))
    while month<1 or month>12:
        month=int(input("Introduzca mes entre 1 y 12: "))
        while day>29 and month==2:
            month=int(input("Introduzca mes entre 1 y 12 (Febrero no puede tener mas de 29 dias): "))
        while day>30 and month in(4,6,9,11):
            month=int(input("Introduzca mes entre 1 y 12 (El mes que has introducido no puede tener mas de 30 dias): "))
    while year<1:
        year=int(input("Introduzca año: "))
    months={1:"ENERO",2:"FEBRERO",3:"MARZO",4:"ABRIL",5:"MAYO",6:"JUNIO",7:"JULIO",8:"AGOSTO",9:"SEPTIEMBRE",10:"OCTUBRE",11:"NOVIEMBRE",12:"DICIEMBRE"}
    if day<0:
        print("Saliendo...")
    else:
        print(f"La fecha en formato largo es {day} de {months[month]} de {year}")
    month=0
    year=0


"""4. Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.
"""

pares=""
lista=[]
numero=int(input("Ve metiendo numeros: "))
while numero >-1:
    lista.append(numero)
    numero=int(input("Ve metiendo numeros: "))

for x in range(len(lista)):
    if lista[x]%2==0 and (x==len(lista)-2 or x==len(lista)-1):
        pares+=str(lista[x])
    elif lista[x]%2==0:
        pares+=str(lista[x])+", "
print(pares)
print(f"El numero mayor es: {conocer('MAYOR',lista)} y los numeros pares son {pares}")

"""5. Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a',
'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di']."""

#lista=["Di","Buen","DIA","a","papa"]

def invertir(lista):
    listainvertida=[]
    for i in range(len(lista)-1,-1,-1):
        listainvertida.append(lista[i])
    return listainvertida

#print(invertir(lista))

"""6. Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario.
"""

#lista=[1,2,3,4,5,6,7,8]
def estaOrdenada(lista):
    estado=True
    #Ordenar Numeros
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            estado=False
    return estado
#print(estaOrdenada(invertir(lista)))

"""7. Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato
[3,4] [2,5]"""

pieza1=["5"," "]
pieza2=["2","5"]
def encajan(a,b):
    encaja=""
    if a[0]==b[0] or a[1]==b[1] or a[0]==b[1] or a[1]==b[0]:
        encaja="ENCAJAN"
    else:
        encaja="NO ENCAJAN"
    return encaja

print(encajan(pieza1,pieza2))

"""8. Realiza un programa que añada números enteros a una lista hasta que se
introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números."""

#numero=int(input("Ve metiendo numeros: "))
#lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
while numero >-1:
    lista.append(numero)
    numero=int(input("Ve metiendo numeros: "))

def comprobarPrimos(lista):
    primo=[]
    resto=0
    contador=0
    for i in range(len(lista)-1):
        contador=0
        for x in range(2,lista[i]):
            resto=lista[i]%x
            if resto==0:
                contador+=1
        if contador==0:
            primo.append(lista[i])
    return primo
def sumar(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma

def promedio(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    promedio=(suma/(len(lista)))
    return promedio

def factorial(lista):
    factorial=1
    factorizado=""
    for i in lista:
        for x in range(i,1,-1):
            factorial+=i*x
        if i==len(lista):
            factorizado+=str(factorial)
        else:
            factorizado+=str(factorial)+", "
    return factorizado

print(comprobarPrimos(lista))
print(sumar(lista))
print(promedio(lista))
print(factorial(lista))

""". Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k."""

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,24]
k=12

def menores(lista,n):
    menores=[]
    for i in range(len(lista)):
        if lista[i] < n:
            menores.append(lista[i])
    return menores
def mayores(lista,n):
    mayores=[]
    for i in range(len(lista)):
        if lista[i] > n:
            mayores.append(lista[i])
    return mayores
def multiplos(lista,k):
    multiplos=[]
    for i in lista:
        if i%k==0:
            multiplos.append(i)
    return multiplos


print(menores(lista,k))
print(mayores(lista,k))
print(multiplos(lista,k))

"""10. Diseña una función conversor que convierta un número de binario a decimal o de
decimal a binario. Esta función recibirá un número en formato de cadena de texto
cuya última posición indica el sistema numérico utilizado (D-decimal, B-binario).
Debe validar la información, así, por ejemplo, el número '1020101B' no sería válido
puesto que los valores en binario son 0 y 1."""

def inverso(cadena):
    inverso=""
    for i in range((len(cadena))-1,-1,-1):
        inverso+=str(cadena[i])
    return inverso
def convertirBIN(numero):
    conversion=0
    posicion=(len(numero))-2
    exponente=0
    try:
        if numero[-1]=="B":
            while posicion > -1:
                conversion+=int(numero[posicion])*(2**exponente)
                posicion-=1
                exponente+=1
            for i in range(len(numero)-1):
                if int(numero[i])!=0 and int(numero[i])!=1:
                    conversion="Los numeros binarios solo contienen 0 o 1"
        elif numero=="0D":
            conversion=0        
        elif numero[-1]=="D":
            entero=0
            entero=int(numero[0:len(numero)-1])
            binario=""
            while (entero!=0):
                binario+=str(entero%2)
                entero=entero//2
            conversion=inverso(binario)
        else:
            conversion="Introduce valores correctos (ej: 111B para binario-decimal o 256D para decimal-binario)"
    except:
        conversion="Introduce valores correctos (ej: 111B para binario-decimal o 256D para decimal-binario)"

    return conversion

#print(convertirBIN(""))

"""11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno."""

lista1=[1,2,3,4,5,5,6,6,9,6,9,10,10]
lista2=[4,5,5,6,6,7,8,6,9,9,10,10]
def intersect(lista1,lista2):
    common=[]
    added=[]
    for i in lista1:
        if i in lista2 and i not in added:
            common.append(i)
            added.append(i)
    return common
#print(intersect(lista1,lista2))

"""12. Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos).
"""

def unionListas(lista1,lista2):
    lista1.extend(lista2)
    union=[]
    for i in lista1:
        if i not in union:
            union.append(i)     
    return union 



#print(unionListas(lista1,lista2))

"""13. Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos."""

nombres=["Juan","Pepe","Juan","Jose","Antonio","Manuel","Almudena","Epifania","Esther","Micaela"]
def devolverNombres(lista,letra):
    try:
        listaDef=[]
        restricciones="1234567890!·$%&/()=?¿Çç*+^`¨´´';,.-_}{][|@#\ºª¬ "
        if letra in restricciones:
            listaDef="El segundo atributo debe ser una letra"
        else:
            for i in lista:
                if i[0].upper()==letra.upper():
                    listaDef.append(i)
        for i in lista:
            for x in range(len(i)):
                if i[x] in restricciones:
                    listaDef="Los nombres no pueden contener numeros"
    except:
        listaDef="Los nombres solo pueden contener caracteres alfabeticos A-Z"
    return listaDef

print(devolverNombres(nombres,"M"))

"""14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos ."""

cadenas=["Unos","Llevan","La","Cadena","Y","Otros","Pagaran","Pagaren","Pagarin","El","Daño"]

def buscarLarga(cadena):
    caracteres2=0
    cadenalarga=""
    comparador=[]
    repetidos=0
    repetidos2=0
    for i in cadena:
        caracteres=len(i)
        if caracteres > caracteres2:
            caracteres2=caracteres
            cadenalarga=i
    for i in cadena:
        if len(cadenalarga) == len(i):
            comparador.append(i)
    for i in comparador:
        repetidos=0
        for x in range(len(i)):
            for z in range(1,len(i)):
                if i[x]==i[z]:
                    repetidos+=1
        if repetidos > repetidos2:
            repetidos2=repetidos
            palabra=i
    return palabra

print(buscarLarga(cadenas))