temperatura = float(input("ingrese el valor numerico de la temperatura: "))

cof = raw_input("escriba la letra c si la temperatura esta en celsius o f si esta en fahrenheit: ")

resultado = 0

if(str(cof) == "c"):

    resultado = ((temperatura*9)/5)+32

    print(str(temperatura)+" °C en grados fahrenheit es igual = "+str(resultado))

else:

    resultado = (((temperatura-32)*5)/9)

    print(str(temperatura)+" °F en grados celsius es igual = "+str(resultado))
