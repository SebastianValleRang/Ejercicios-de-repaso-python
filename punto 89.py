nestu = input("ingrese el numero de estudiantes: ")

archivo = open('DatosEjercicio89.txt','w')

a = int(nestu)
b = 0
c = 0

nota1aux = 0
nota2aux = 0
nota3aux = 0
nota4aux = 0


matriz = []

for i in range(a):
    
    matriz.append([0]*11)
        

for i in range(0,a):

    print("informacion del estudiante No."+str(i+1)+": ")

    codigo   = str(input("ingrese el codigo del estudiante: "))
    nombre   = str(input("ingrese el nombre del estudiante: "))
    apellido = str(input("ingrese el apellido del estudiante: "))
    carrera  = str(input("ingrese la carrera del estudiante: "))
    estado   = str(input("ingrese el estado del estudiante: "))

    nota1   = str(input("ingrese la primera nota del estudiante: "))
    nota2   = str(input("ingrese la segunda nota del estudiante: "))    
    nota3   = str(input("ingrese la tercera nota del estudiante: "))
    nota4   = str(input("ingrese la cuarta nota del estudiante: "))

    matriz[i][0] = codigo
    matriz[i][1] = nombre
    matriz[i][2] = apellido
    matriz[i][3] = carrera
    matriz[i][4] = estado
    
    matriz[i][5] = nota1
    matriz[i][6] = nota2
    matriz[i][7] = nota3
    matriz[i][8] = nota4

archivo = open('DatosEjercicio89.txt', 'a+')

archivo.write("Codigo, Nombre, Apellido, Carrera, Estado, nota 1, nota 2, nota 3, nota 4 \n")

for i in range(a):
    for j in range(11):
        
        archivo.write(str(matriz[i][j])+", ")
    archivo.write("\n")


archivo.close()


while(c != 1):

    opcion = int(input(" 1)modificar, 2)eliminar o 3)para cerrar el programa: "))

    b = 0
#------------------------------------------------------------------------------------------------------------------------------------------------------ 

    if( opcion == 1 ):

        codigomodi = str(input("ingrese el codigo del estudiante a modificar: "))

        for i in range(0,a):

            if(matriz[i][0] == codigomodi):

                b = i

        quemodi = str(input("que desea modificar: 1)codigo, 2)nombre, 3)apellido, 4)carrera, 5)estado:, 6)nota No.1, 7)nota No.2, 8)nota No.3 o 9)nota No.4 "))

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
            
        if( opcion == 6 ):

            matriz[b][5] = str(input("ingrese la nueva nota No.1 del estudiante: "))
            
        if( opcion == 7 ):

            matriz[b][6] = str(input("ingrese la nueva nota No.2 del estudiante: "))
            
        if( opcion == 8 ):

            matriz[b][7] = str(input("ingrese la nueva nota No.3 del estudiante: "))
            
        if( opcion == 9 ):

            matriz[b][8] = str(input("ingrese la nueva nota No.4 del estudiante: "))

        archivo = open('DatosEjercicio89.txt', 'a+')    

        for i in range(a):
            for j in range(11):
        
                archivo.write(str(matriz[i][j])+", ")
                
            archivo.write("\n")


        archivo.close()

        
#------------------------------------------------------------------------------------------------------------------------------------------------------        

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
                matriz[i][5] = "0"
                matriz[i][6] = "0"
                matriz[i][7] = "0"
                matriz[i][8] = "0"
                matriz[i][9] = "0"
                matriz[i][10] = "0"

        archivo = open('DatosEjercicio89.txt', 'a+')
    
        for i in range(a):
            for j in range(11):
        
                archivo.write(matriz[i][j]+", ")
                
            archivo.write("\n")


        archivo.close()


#------------------------------------------------------------------------------------------------------------------------------------------------------                

    if( opcion == 3 ):

        c = 1

for i in range(a):

    if(matriz[i][5] != "eliminado"):

        nota1aux = float(matriz[i][5])
        nota2aux = float(matriz[i][6])
        nota3aux = float(matriz[i][7])
        nota4aux = float(matriz[i][8])
    
        matriz[i][9] = str((nota1aux+nota2aux+nota3aux+nota4aux)/4)

        if(float(matriz[i][9]) >= 3):

            matriz[i][10] = "Pasó"

        else:

            matriz[i][10] = "No pasó"
            

archivo = open('DatosEjercicio89.txt', 'w')

archivo.write("Codigo, Nombre, Apellido, Carrera, Estado, nota 1, nota 2, nota 3, nota 4, promedio, situiacion de la materia \n")

for i in range(a):
    for j in range(11):
        
        archivo.write(matriz[i][j]+", ")
                
    archivo.write("\n")

archivo.close()




    


















        
