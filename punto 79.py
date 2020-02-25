def sumarecursiva(numero):

    if(numero == 1):

        return 1

    else:

        return numero + sumarecursiva(numero-1)



numero = int(input("ingrese un numero natural: "))

print("la suma de numeros desde el 1 hasta "+str(numero)+" es de: "+str(sumarecursiva(numero)))



    
