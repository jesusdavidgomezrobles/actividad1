
num = int(input("Ingrese un numero"))

def numero_perfecto(num):
    suma = 0
    
    
    for i in range(1, num):
        if num%i==0:
            suma += i
        
    return suma == num

if (numero_perfecto(num)==True):
    print("El numero ingresado(" + str(num) + ")es perfecto")
else:
    print("El numero ingresado(" + str(num) + ")no es perfecto")
