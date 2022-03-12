j=0
# PROBLEMA
j=j+1
print(f"\nEJERCICIO N°{j}")
name=input("Ingrese nombre: ")
print(f"¡ Hola {name} !")



# PROBLEMA 2
j=j+1
print(f"\nEJERCICIO N°{j}")
nShows=int(input("¿Cuantos show musicales a visto?: "))
if nShows>3:
    print(True)
else:
    print(False)



# PROBLEMA 3
j=j+1
print(f"\nEJERCICIO N°{j}")
n=float(input("Ingrese numero con decimales: "))
m=int(input("Ingrese numero Entero: "))
suma=n+m
print(f"El resultado de la suma es: {suma}")



# PROBLEMA 4
j=j+1
print(f"\nEJERCICIO N°{j}")
n=int(input("Ingrese numero payasos: "))
m=int(input("Ingrese numero muñecas: "))
peso=112*n+75*m
print(f"El peso del paquete es: {peso}g")



# PROBLEMA 5
j=j+1
print(f"\nEJERCICIO N°{j}")
n=int(input("Ingrese valor N°: "))
sumaN=n*(n+1)//2
print(f"La suma de los {n} primeros numeros es: {sumaN}")



# PROBLEMA 6
j=j+1
print(f"\nEJERCICIO N°{j}")
edad=int(input("Ingrese edad: "))
cant=int(input("Cantidad de productos comprados: "))
if edad>=18 and cant>1:
    print(True)
else:
    print(False)



# PROBLEMA 7
j=j+1
print(f"\nEJERCICIO N°{j}")
n1=float(input("Ingrese 1er Numero: "))
n2=float(input("Ingrese 2do Numero: "))
if n1>n2:
    print(f"El numero mayor es: {n1}")
elif n2>n1:
    print(f"El numero mayor es: {n2}")
else:
    print("Los numeros son iguales")



# PROBLEMA 8
j=j+1
print(f"\nEJERCICIO N°{j}")
n1=float(input("Ingrese Dividendo: "))
n2=float(input("Ingrese Divisor: "))

if n2==0:
    print(f"El Divisor no puede ser cero")
else:
    q=n1/n2
    print(f"La division es: {q}")



# PROBLEMA 9
j=j+1
print(f"\nEJERCICIO N°{j}")
let=input("Ingrese una letra: ")
tamaño=len(let)
if tamaño==1:
    if (let=='a' or let=='e' or let=='i' or let=='o' or let=='u'):
        print("La letra es una vocal")
    else:
        print("La letra en una consonante")
else:
    print("Error: Se ha ingresado un texto")



# PROBLEMA 10
j=j+1
print(f"\nEJERCICIO N°{j}")
año=float(input("Ingrese el año: "))
if (año%4==0 and año%100!=0) or (año%400==0):
    print(f"El año es BISIESTO")
else:
    print(f"El año NO ES BISIESTO")



# PROBLEMA 11
j=j+1
print(f"\nEJERCICIO N°{j}")
edad=int(input("Ingrese su edad: "))
if (edad<=4):
    print("precio a pagar: GRATIS")
elif(edad>4 and edad<=18):
    print("precio a pagar: 5 soles")
elif(edad>18 and edad<100):
    print("precio a pagar: 10  soles")
else:
    print("Edad ingresada INCORRECTA")



# PROBLEMA 12
j=j+1
print(f"\nEJERCICIO N°{j}")
print("Ingrese los elementos de la lista original")
l1=input("1er elemento: ")
l2=input("2do elemento: ")
l3=input("3er elemento: ")
l4=input("4to elemento: ")
l5=input("5to elemento: ")
l6=input("6to elemento: ")

lista=[l1,l2,l3,l4,l5,l6]
lista.reverse()
print(lista)



# PROBLEMA 13
j=j+1
print(f"\nEJERCICIO N°{j}")
lista=[l1,l2,l3,l4,l5,l6]
lista.remove(l1)
lista.remove(l5)
lista.remove(l6)
print(lista)



# PROBLEMA 14
j=j+1
print(f"\nEJERCICIO N°{j}")
lista=[1,1,2,3,4,4,5,1]
tam=int(input("Longitud de la primera lista:"))
lista1=lista[:tam]
lista2=lista[tam:]
print(f"Lista 1: {lista1} ")
print(f"Lista 2: {lista2} ")



#Problema 15
j=j+1
print(f"\nEJERCICIO N°{j}")
lista=['rojo','verde','blanco','negro','naranja']
print(lista)
elemento=input("Elemento a mover al ultimo:")
lista.append(lista.pop(lista.index(elemento)))
print(lista)