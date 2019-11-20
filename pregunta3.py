datos = []
for i in range(5):
    nombre = input("Ingrese su nombre porfavor: ")
    sexo = input("Ingrese su sexo porfavor M/F: ") 
    edad = int(input("Ingrese su edad porfavor"))
    
    if 5 <= edad <= 17:
        n = datos.append(nombre)
        d = datos.append(edad)
        
    else:
        print("Debe ser mayor o igual a 5 ó menor o igual que 17 años, ingrese nuevamente el dato")
    
    
    if sexo == "m":
        datos.append(sexo)
        m = datos.count(sexo)
    elif sexo == "f":
        datos.append(sexo)
        f = datos.count(sexo)
    else:
        print("Dato erroreneo, seleccione nuevamente")

    
promedio = (datos[1]+datos[4]+datos[7]+datos[10]+datos[13])/2
print(datos)
print("Hay ", m, "hombres y hay",f , "mujeres ")
print("El promedio de edad es: ", promedio)