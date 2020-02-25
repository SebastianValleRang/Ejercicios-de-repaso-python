nestu = input("ingrese el numero de estudiantes: ")

archivo = open('datos.txt','w')

a = int(nestu)
b = 0
c = 0
matriz = []

for i in range(a):

    matriz.append([0]*5)

for i in range(0,a):

    print("informacion del estudiante No."+str(i+1)+": ")

    codigo   = str(input("ingrese el codigo del estudiante: "))
    nombre   = str(input("ingrese el nombre del estudiante: "))
    apellido = str(input("ingrese el apellido del estudiante: "))
    carrera  = str(input("ingrese la carrera del estudiante: "))
    estado   = str(input("ingrese el estado del estudiante: "))

    matriz[i][0] = codigo
    matriz[i][1] = nombre
    matriz[i][2] = apellido
    matriz[i][3] = carrera
    matriz[i][4] = estado

archivo = open('DatosEjercicio88.txt', 'a+')

archivo.write("Codigo, Nombre, Apellido, Carrera, Estado \n")

for i in range(a):
    for j in range(5):
        
        archivo.write(matriz[i][j]+", ")
    archivo.write("\n")


archivo.close()


while(c != 1):

    opcion = int(input(" 1)modificar, 2)eliminar o 3)para cerrar el programa: "))

    b = 0
#------------------------------------------------------------------------------------------------ 

    if( opcion == 1 ):

        codigomodi = str(input("ingrese el codigo del estudiante a modificar: "))

        for i in range(0,a):

            if(matriz[i][0] == codigomodi):

                b = i

        quemodi = str(input("que desea modificar: 1)codigo, 2)nombre, 3)apellido, 4)carrera o 5)estado: "))

        if( opcion == 1 ):

            matriz[b][0] = str(input("ingrese el nuevo codigo del estudiante: "))
            
        if( opcion == 2 ):

            matriz[b][1] = str(input("ingrese el nuevo nombre del estudiante: "))
            
        if( opcion == 3 ):

            matriz[b][2] = str(input("ingrese el nuevo apellido del estudiante: "))
            
        if( opcion == 4 ):

            matriz[b][3] = str(input("ingrese el nueva carrera del estudiante: "))
            
        if( opcion == 5 ):

            matriz[b][4] = str(input("ingrese el nuevo estado del estudiante: "))


        for i in range(a):
            for j in range(5):
        
                archivo.write(matriz[i][j]+", ")
                
            archivo.write("\n")


        archivo.close()

        
#------------------------------------------------------------------------------------------------        

    if( opcion == 2 ):

        codigoelim = str(input("ingrese el codigo del estudiante a eliminar: "))

        for i in range(0,a):

            if(matriz[i][0] == codigoelim):

                b = i
                
                matriz[i][0] = "eliminado"
                matriz[i][1] = "0"
                matriz[i][2] = "0"
                matriz[i][3] = "0"
                matriz[i][4] = "0"

        for i in range(a):
            for j in range(5):
        
                archivo.write(matriz[i][j]+", ")
                
            archivo.write("\n")


        archivo.close()


#------------------------------------------------------------------------------------------------                
    if( opcion == 3 ):

        c = 1


        
    
