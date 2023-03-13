'''Aplicación 2. Escriba un algoritmo que determine
la categoría deportiva de un usuario en función de su edad.
Menor de 7 años: “benjamín”
8 a 9 años: “ alevín”
10 a 11 años: “infantil”
12 años y más: “cadete”
'''

edad = int(input ("Dime tu edad: "))

if (edad <= 7):
    print("Eres benjamín")
    
elif(edad <= 9):
    print("Eres alevín")
    
elif(edad <= 11):
    print("Eres infantil")
    
else:
    print("Eres cadete")
    
