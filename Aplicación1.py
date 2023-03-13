'''Aplicación 1.
escriba, usando comparaciones,
un algoritmo que muestre
el estado del agua
(hielo,líquido,vapor)
en función de su temperatura'''

temp = int(input ("temperatura del agua: "))

if (temp >= 100 ):
    print ("Vapor")
    
elif ( temp < 0):
    print("Hielo")
    
else:
    print("Líquido")
    
