menu="""
1. Llenar tanque(diesel o gasolina)
2. Asignar coche a surtidor y repostar
3. Ver puntos de cliente
4. Comprobar histórico de ventas.
5. Consultar estado de surtidores
6. Asignar precio a la gasolina
7. Asignar precio al diesel
8. Salir"""



baseCoches={"1234AAA":"DIESEL"}
basePuntos={"1234AAA":0}
baseConsumo={"1234AAA":0}
capacidad1, capacidad2, capacidad3, capacidad4=5000, 5000, 5000, 5000
distribuido1, distribuido2, distribuido3, distribuido4=0, 0, 0, 0
precio_diesel, precio_gasolina=0, 0
while precio_diesel<1 or precio_gasolina<1:
    precio_diesel=round(float(input("Introduzca precio Diesel: ")),3)
    precio_gasolina=round(float(input("Introduzca precio Gasolina: ")),3)

def registrar_coche(matricula,baseCoches=baseCoches,basePuntos=basePuntos,baseConsumo=baseConsumo):
    combustible=""
    while matricula[:4]not in "1234567890" or matricula[-3:].upper() in "1234567890!·$%&/()=?¿Çç*+^`¨´´';,.-_}{][|@#\ºª¬ ":
        matricula=input("La matricula debe ser XXXXAAA: ")
    while combustible!="DIESEL" and combustible!="GASOLINA":
        combustible=input("Elige tipo de combustible. DIESEL o GASOLINA: ").upper()
    baseCoches[matricula]=combustible
    basePuntos[matricula]=0
    baseConsumo[matricula]=0

def llenar_surtidor(surtidor,cantidad, tanque1=capacidad1, tanque2=capacidad2,tanque3=capacidad3,tanque4=capacidad4):
    while cantidad<0 or cantidad > 5000:
        cantidad=int(input("Introduce una cantidad entre 0 y 5000: "))
    while surtidor<0 or surtidor > 4:
        surtidor=int(input("Elige surtidor correcto, 1, 2, 3 o 4: "))
    if surtidor==1 and tanque1+cantidad<=5000:
        tanque1+=cantidad
    elif surtidor==2 and tanque2+cantidad<=5000:
        tanque2+=cantidad
    elif surtidor==3 and tanque3+cantidad<=5000:
        tanque3+=cantidad
    elif surtidor==4 and tanque4+cantidad<=5000:
        tanque4+=cantidad
    else:
        print("El tanque excede la capacidad maxima")

def comprobar_matricula(matricula):
    while matricula[:4]not in "1234567890" or matricula[-3:].upper() in "1234567890!·$%&/()=?¿Çç*+^`¨´´';,.-_}{][|@#\ºª¬ ":
        matricula=input("La matricula debe ser XXXXAAA: ")
    return matricula

def repostar(cuantia,tipo,precio_diesel=precio_diesel,precio_gasolina=precio_gasolina,
capacidad1=capacidad1,capacidad2=capacidad2,capacidad3=capacidad3,capacidad4=capacidad4,
distribuido1=distribuido1,distribuido2=distribuido2,distribuido3=distribuido3,distribuido4=distribuido4):
    if tipo=="DIESEL":
        precio=precio_diesel
        if capacidad3<capacidad4:
            capacidad4=capacidad4-(cuantia*precio)
            distribuido4=distribuido4+(cuantia*precio)
            
        else:
            capacidad3=capacidad3-(cuantia*precio)
            distribuido3=distribuido3+(cuantia*precio)
            
    
    elif tipo=="GASOLINA":
        precio=precio_gasolina
        if capacidad1<capacidad2:
            capacidad2=capacidad2-(cuantia*precio)
            distribuido2=distribuido2+(cuantia*precio)
            
        else:
            capacidad1=capacidad1-(cuantia*precio)
            distribuido1=distribuido1+(cuantia*precio)
    return cuantia*precio

opcion=0
print(menu)
while opcion!=8:
    opcion=int(input("Introduce opcion: "))
    if opcion==1:
        llenar_surtidor(int(input("¿Que surtidor va a rellenar?")), int(input("Introduce cantidad a rellenar: ")))
    elif opcion==2:
        matricula=comprobar_matricula(input("Introduce matricula en formato XXXXAAAA: "))
        if matricula not in baseCoches:
            registrar_coche(matricula)
            tipo=baseCoches.get(matricula)
            while cuantia < 10:
                cuantia=round(float(input(f"¿Cuanto va a repostar(min 10€): ")),2)
            baseConsumo[matricula]=baseConsumo.get(matricula)+repostar(cuantia,tipo)
        else:
            tipo=baseCoches.get(matricula)
            cuantia=0
            while cuantia < 10:
                cuantia=round(float(input(f"¿Cuanto va a repostar(min 10€): ")),2)
            baseConsumo[matricula]=baseConsumo.get(matricula)+repostar(cuantia,tipo)
                    
            basePuntos[matricula]=basePuntos.get(matricula)+(cuantia//20)
    elif opcion==3:
        matricula=comprobar_matricula(input("Introduce matricula en formato XXXXAAAA: "))
        if matricula not in baseCoches:
            print("No es cliente")
        else:
            print(f"Tiene {basePuntos.get(matricula)} puntos")
    elif opcion==4:
        print(baseConsumo.get(comprobar_matricula(input("Introduce matricula en formato XXXXAAAA: "))))
    elif opcion==5:
        print(distribuido1,distribuido2,distribuido3,distribuido4)
    elif opcion==6:
        precio_gasolina=0
        while precio_diesel<1 or precio_gasolina<1:
            precio_gasolina=round(float(input("Introduzca precio Gasolina: ")),3)
    elif opcion==7:
        precio_diesel=0
        while precio_diesel<1 or precio_gasolina<1:
            precio_diesel=round(float(input("Introduzca precio Diesel: ")),3)
         
