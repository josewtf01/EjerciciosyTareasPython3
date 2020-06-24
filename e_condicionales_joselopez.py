# condicional de numero negativo, positivo o cero
w = -3

if  w == 0:
    print("el número es cero\n")
elif w < 0 :
    print("el número es negativo\n")
else:
    print("el número es positivo\n")

# condicional de número par o impar
z = 4

if z % 2 == 0:
    print("el número es par\n")
else:
    print("el número es impar\n")

# condicional de número primo
x = 5

if x > 1:
   for i in range(2,x):
       if (x % i) == 0:
           print(x,"no es un número primo\n")
           print(i,"veces",x//i,"es",x,"\n")
           break
   else:
       print(x,"es un número primo\n")
else:
   print(x,"no es un número primo\n")

#ingreso de un número
print("ingresar un número:\n")
numeroIngresado = int(input())

#condicional de año bisiesto

y = 1902

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(y," es un año bisiesto\n")
        else:
            print(y," no es un año bisiesto\n")
    else:
        print(y," es un año bisiesto\n")
else:
    print(y," no es un año bisiesto\n")


def evaluacion():
    #ingreso de un número
    print("ingresar un número:\n")
    num = int(input())

    # condicional de numero negativo, positivo o cero
    if  num == 0:
        print("el número es cero\n")
    elif num < 0 :
        print("el número es negativo\n")
    else:
        print("el número es positivo\n")

    # condicional de número par o impar

    if num % 2 == 0:
        print("el número es par\n")
    else:
        print("el número es impar\n")

    #condicional de número primo
    if num > 1:
       for i in range(2,x):
           if (num % i) == 0:
               print(num,"no es un número primo\n")
               print(i,"veces",num//i,"is",num,"\n")
               break
       else:
           print(num,"es un número primo","\n")
    else:
       print(num,"no es un número primo","\n")
