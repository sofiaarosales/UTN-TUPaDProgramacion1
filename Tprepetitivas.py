#Ejercicio 1
for i in range(101):
    print(i)

#Ejercicio 2
numero = int(input("Ingrese un numero: "))  
numero = abs(numero)  
contador_digitos = 0
if numero == 0:
    contador_digitos = 1
else:
    while numero > 0:
        numero = numero // 10
        contador_digitos += 1
print(f"El numero ingresado tiene {contador_digitos} digitos.") 

#Ejercicio 3
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
menor = min (num1, num2)
mayor = max (num1, num2)

suma_total = 0

for i in range(menor + 1, mayor):
    suma_total += i

print(f"La suma entre los numeros {menor} y {mayor} (excluyendolos) es: {suma_total} ")

#Ejercicio 4
total_acumulado = 0

print("Calculadora activada (Ingresa un 0 cuando quieras detenerte y ver el total)")

while True:
    numero = int(input("Ingrese un numero entero: "))

    if numero == 0:
        print("Cero ingresado. Cerrando la suma...\n")
        break

    total_acumulado += numero

    print(f"El total acumulado es: {total_acumulado}")

#Ejercicio 5
import random  

numero_secreto = random.randint(0, 9)

intentos = 0

print("🎮 ¡Bienvenida al juego de adivinanzas!")
print("Estoy pensando en un número del 0 al 9. ¿Podés adivinar cuál es?")

while True:
    jugada = int(input("Ingresá tu número: "))
    
   
    intentos += 1  
    
    if jugada == numero_secreto:
        print(f"\n¡BINGO! Acertaste, el número era el {numero_secreto}.")
        print(f"🏆 Te tomó un total de {intentos} intento(s) ganar el juego.")
        break  # Rompemos el bucle porque ya ganó
    else:
        print("Mmm no, ese no es. ¡Volvé a intentarlo!")

#Ejercicio 6
for i in range(100, -1, -2):
    print(i)

    numero = 100

#Ejercicio 7
limite = int(input("Ingresá un número entero positivo: "))

suma_total = 0

for i in range(limite + 1):
    suma_total += i

print(f"La suma de todos los números entre 0 y {limite} es: {suma_total}")

#Ejercicio 8
# Cambiá este 5 por un 100 cuando quieras entregar el programa final
CANTIDAD_NUMEROS = 5 

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"--- Ingresá {CANTIDAD_NUMEROS} números ---")

for i in range(CANTIDAD_NUMEROS):
    num = int(input(f"Número {i + 1}: "))
    

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
        
   
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
   

print("\n--- Resultados ---")
print(f"Pares: {pares} | Impares: {impares}")
print(f"Positivos: {positivos} | Negativos: {negativos}")

#Ejercicio 9
CANTIDAD_NUMEROS = 5
suma_total = 0

print(f"--- Calculadora de Promedio ({CANTIDAD_NUMEROS} valores) ---")

for i in range(CANTIDAD_NUMEROS):
    num = int(input(f"Ingresá el valor {i + 1}: "))
    suma_total += num

media = suma_total / CANTIDAD_NUMEROS

print(f"\nLa media (promedio) de los números ingresados es: {media}")

#Ejercicio 10
numero = int(input("Ingresá un número: "))
numero_invertido = 0

while numero > 0:
    
    ultimo_digito = numero % 10
    
    
    numero_invertido = (numero_invertido * 10) + ultimo_digito
    

    numero = numero // 10

print(f"El número invertido es: {numero_invertido}")
    