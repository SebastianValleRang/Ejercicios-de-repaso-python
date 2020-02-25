def fibo(n):

    if(n == 0):

        return 0


    if(n == 1):

        return 1

    else:

        return fibo(n-2) + fibo(n-1)



n = int(input("ingrese el n termino que desea saber de fibonacci: "))

print("el n termino de la serie es: "+str(fibo(n)))
