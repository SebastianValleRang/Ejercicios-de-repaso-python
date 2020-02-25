inicial = list(str(input("escriba la primera frase: ")))

matriz=[]

comprobacion = 0

longitud2 = int(len(inicial))
longitud = int(len(inicial))

for i in range(2):

    matriz.append([""]*longitud)

for i in range(longitud):

    matriz[0][i] = inicial[i]

for i in range(0,longitud):   

    longitud = longitud-1
    matriz[1][i] = inicial[longitud]

for i in range(0,longitud2):

    if(matriz[0][i] != matriz[1][i]):

        comprobacion = 1

if(comprobacion == 1):

    print ("No es palindroma")
    
else:
    
    print ("Es palindroma")



