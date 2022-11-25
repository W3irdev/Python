"""1. Design a function called charactersInString that has a character string and a character as 
input parameters and returns how many times that character appears in the string. It should 
do if the string and character are lower case or upper case characters."""

def charactersInString(text,c):
    times=0
    for i in text.lower():
        if i==c.lower():
            times+=1
    return times

if __name__=='__main__':
    print(charactersInString("StrirninggrrrRg","r"))

"""2. Design a function called lowCaseInString that has a string of characters as parameter, the 
method should return how many of those characters are lowcase letters."""

def lowCaseInString(words):
    lowers=0
    for c in words:
        if c==c.lower() and c not in "1234567890!·$%&/()=?¿Çç*+^`¨´´';,.-_}{][|@#\ºª¬ ":
            lowers+=1

    return lowers

if __name__=='__main__':
    print(lowCaseInString("EsToEsunAPRueBA"))

"""3. Design a function called upperCaseInString that has a string of characters as parameter, the 
method should return how many of those characters are upper case letters."""

def upperCaseInString(words):
    uppers=0
    for c in words:
        if c==c.upper() and c not in "1234567890!·$%&/()=?¿Çç*+^`¨´´';,.-_}{][|@#\ºª¬ ":
            uppers+=1

    return uppers

if __name__=='__main__':
    print(upperCaseInString("EsToEsunAPRueBA"))

"""4. Design a function called numberInString that has a string of characters as parameter, the 
method should return how many of those characters are numbers."""

def numberInString(string):
    arenumbers=0
    for c in string:
        if c in "1234567890":
            arenumbers+=1
    return arenumbers

if __name__=='__main__':
    print(numberInString("12aEsToEsunAPRueBA"))

"""5. Design a function called palindrome that has a string of characters as parameter, and return 
true if it is a palindrome or false in other case. A word is a palindrome, if it is reads the 
same from left to right as from right to left, ignoring whites,. For example: "anilina" or "el 
abad le dio arroz al zorro" To simplify the problem, you can assume that simple characters 
are used, that is, without tildes or diresis."""


def palindrome(palabra):
    comprobar=0
    nospace=""
    for i in palabra.lower():
        if i != " ":
            nospace+=i

    for c in range (len(nospace)):
        if nospace[c]==nospace[-c-1]:
            comprobar+=1
    return comprobar==len(nospace)

print(palindrome("Dabale arroz a la zorra el abad"))

"""6. Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si 
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se 
encontrará y deberá devolver True, en caso contrario deberá devolver False."""


def encontrarPalabra(palabra,texto):
    buscar=""
    posicion=0
    contiene=False
    for c in texto:
        if c == palabra[posicion]:
            buscar+=c
            posicion+=1
    if buscar==palabra:
        contiene=True
    
    return contiene

print(encontrarPalabra("hola","shybaoxlna"))

"""7. Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y 
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla por la 
tercera."""

def reemplazarPalabra(texto,palabra,sustituto):
    nuevafrase=""
    es=0
    desplaza=0
    control=0
    if palabra in texto:
        c=0
        while c < len(texto) and control==0:
            if texto[c]==palabra[0]:
                while es < len(palabra):
                    if texto[c+desplaza]==palabra[es]:
                        es+=1
                        desplaza+=1
                if es == len(palabra) and texto[c+len(palabra)]==" ":
                    nuevafrase=nuevafrase + sustituto
                    c+=len(palabra)
                    es=0
                else:
                    nuevafrase="La palabra a sustituir no se encuentra"
                    es=0
                    c+=1
                    control=1
            else:
                nuevafrase+=texto[c]
                c+=1
    return nuevafrase

print(reemplazarPalabra("Homer fue a beber cerveza", "beber", "comprar"))

"""8. Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra 
o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2."""

def contarVocalesDiferentes(frase):
    vocales=[]
    for c in frase:
        if c.lower() in "aeiou" and c.lower() not in vocales:
            vocales+=c

    return len(vocales)

print(contarVocalesDiferentes("murcielago"))

"""9. Crear una función que, tomando una cadena de texto como entrada, construya y devuelva 
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes 
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería 
"crsdprgrmcnuoeoaaio"""

def separadorCaracter(frase):
    separadoconsonante=""
    separadovocales=""
    for c in frase:
        if c.lower() in "aeiou":
            separadovocales+=c
        elif c.lower() == " ":
            separadovocales+=""
        else:
            separadoconsonante+=c
    return separadoconsonante+separadovocales

print(separadorCaracter("curso de programacion"))

"""10. Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco. 
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3"""

def contarPalabras(frase):
    palabras=0
    if frase[0]!=" ":
        palabras+=1
    for c in range(len(frase)-1):
        if frase[c] == " " and frase[c+1] !=" ":
            palabras+=1
        

    return palabras

print(contarPalabras(" Ipsum Lorem  "))
