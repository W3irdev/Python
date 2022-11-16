"""1. Design a method called computeFactorial that receives a positive integer and
returns the factorial for that number. If the number is negative the method should
return None."""

def computeFactorial(number):
    fact=number
    while number > 1:
        number-=1
        fact=fact*number
    return fact

"""2. Design a method called isLeapYear that receives a number and returns False for
common years and True for leap years. You may know that a year is considered to
be a leap year if it is divisible by 4, unless it is also divisible by 100. A year is not a
leap year if it is divisible by 100 unless it is also divisible by 400."""

def isLeapYear(year):
    leap=None
    if (year %4==0) and (year%100!=0 or year%400==0):
        leap=True
    else:
        leap=False
    return leap

"""3. Design a method called computeDaysInMonth that returns the number of days for
the month and year that are received as arguments. You may use the method
leapYear above. If the values are not valid the method should return -1."""

def computeDaysInMonth(month,year):
    monthsdays=[31,28,31,30,31,30,31,31,30,31,30,31]
    days=0
    try:
        if month<1 or year<1:
            days=-1
        else:
            if isLeapYear(year) and month==2:
                days=29
            else:
                days=monthsdays[month-1]
    except:
        days=-1
    return days



"""4. Design a method called getDayOfWeek that receives a list containing three integers
(day, month and year) and returns the day of the week for that date (Monday,
Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).
You can use the following algorithm to get a number between 0 (Sunday) and 6
(Saturday) corresponding to the day in the week for a given date:
a = (14 - month) / 12
y = year – a
m = month + 12 * a – 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7"""

def getDayOfWeek(day,month,year):
    daysmonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    dayinweek={5:"Domingo",6:"Lunes",4:"Martes",5:"Miercoles",2:"Jueves",3:"Viernes",4:"Sabado"}
    try:
        if month<1 or year<1:
            print("Introduzca valores validos")
        else:
            a = (14 - month)/12
            y = year - a
            m = month + 12 * a - 2
            d= int(((day + y + y//4 - y//100 + y//400 + (31*m)//12)%7))
            d=dayinweek[d]
    except:
        print("Valores invalidos")
    return d
print(getDayOfWeek(16,11,2022))

"""5. Design a method called powerIt that receives two integers and raises the first
number to the second. You may use the product or recursion and check the values. If
no exponent is provided the first number is raised to 0.
"""

def multiplicacion(n,m):
    prod=0
    for i in range(m):
        prod=prod+n
    return prod
def elevadoconsuma(base,exp=0):
    total=1
    for i in range(exp):
        total=multiplicacion(base,total)
    return total

def powerIt(base,exponent=0):
    total=1

    for i in range(exponent):
        total=base*total
    
    return total

#print(elevadoconsuma(5,5))

"""6. Design a method called getNumberOfDigits that receives one number (it can be
real, integer, positive or negative) and should return the number of digits it contains. If
the parameter is not valid the method should return None. Extend this function to
other numeric systems (hexadecimal, decimal, binary, octal).
"""

def getNumberOfDigits(number):
    digitos=None
    txt=str(number).upper()
    contador=0
    try:
        if "." in txt:
            digitos=len(txt)-1
        elif "." in txt and "-" in txt:
            digitos=(len(txt))-2
        else:
            digitos=len(txt)
        for char in txt:
            if char in "GHIJKLMNOPQRSTUVWXYZ":
                digitos=None
            elif char ==".":
                contador+=1
                if contador>1:
                    digitos=None
        if digitos==0:
            digitos=None
    except ValueError:
        digitos=None


    return digitos


print(getNumberOfDigits(""))

"""7. Design a method called isPrime that receives one integer positive number greater
than 0 as parameter. The method should return True if the number is prime or False if
not prime. If the parameter is not valid the method should return None."""

def isPrime(number):
    if number>0:
        try:
            prime=True
            for i in range(2,number):
                if number%i==0:
                    prime=False
        except:
            prime=None
    else:
        prime="Introduce un numero mayor a 0"
    return prime
    
print(isPrime(2))


"""8. Design a method called solveSecondOrderEquation that receives three integer
positive numbers corresponding to the coefficients of a second order equation
(ax2+bx+c=0) and computes its possible solutions. If the parameters are not valid the
method should return None.
"""

def solveSecondOrderEquation(a,b,c):
    try:
        x1=(-b+(((b**2)-4*a*c)**0.5))/2*a
        x2=(-b-(((b**2)-4*a*c)**0.5))/2*a
        solucion=x1,x2
    except:
        solucion=None

    return solucion


print(solveSecondOrderEquation(True,"2",6))

"""9. Design a method called getPrimeDivisors that receives a positive number as a
parameter and returns a list containing its prime divisors. If the parameter is not valid
the method should return None.
"""
def getPrimeDivisors(a):
    primes=[]
    for i in range(1,a):
        if a%i==0 and isPrime(i):
            primes.append(i)

    return primes

print(getPrimeDivisors(9999999))


"""10. Design a method called isFriendNumber that receives two positive numbers and
returns True if the numbers are friends, False otherwise. Two numbers are
considered to be friends if the sum of its divisors, except the given number, is equal
to the second and vice versa."""

def isFriendNumber(a,b):
    divisors=[]

    for i in range(1,a-1):
        if a%i==0:
            divisors.append(i)
    if sum(divisors)==b:
        isFriend=True
    else:
        isFriend=False
    return isFriend
    
print(isFriendNumber(284,220))