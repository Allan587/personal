import math
print ("Bienvenidos al cajero automático de Andrey")

opf = 0; opf2 = 0; opf3 = 0; opf4 = 0 

d = float(input("Ingrese la cantidad de dinero que desee retirar: "))        
    
if d >= 10000 :
    opf = math.trunc(d / 10000)
    d = (d - (opf * 10000))
else:
    pass 

if  d <= 9000: 
    opf2 = math.trunc(d / 5000)
    d = (d - (opf2 * 5000))
else:
    pass
        
if  d <= 4000: 
    opf3 = math.trunc(d / 2000)
    d = (d - (opf3 * 2000))
else:
    pass
    
if d == 1000 : 
    opf4 = math.trunc(d / 1000)
    d = (d - (opf4 * 1000))
else:
    pass
    
print (f"La cantidad de billetes que corresponden según el monto solicitado son: \n {opf} de 10.000 colones \n {opf2} de 5.000 colones \n {opf3} de 2.000 colones \n {opf4} de 1.000 colones")