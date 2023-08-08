# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
20/07/2023

Metodo de Newton Raphson Copmlejos
"""

from pylab import *
from tabulate import tabulate

def newtonRaphson(f, fprima, x0, n, d):
        """Es un algoritmo numérico para encontrar raíces de funciones continuas y diferenciables. 
        Se basa en utilizar la tangente a la curva de la función en un punto cercano a la raíz 
        como una aproximación lineal de la función. Luego, se encuentra el punto donde esta 
        tangente cruza el eje x y se repite el proceso para obtener una aproximación mejorada. 
        Requiere un valor inicial de aproximación y la derivada de la función en el punto dado."""
    
        #xi = float(x0)
        
        xi = x0
        
        tabla = [['i','xi','ea'],[0,xi,]]
        
        for i in range(n):
            
            x = xi
            fxi = eval(f)
            
            if fxi == 0:
                break
            
            fprimaxi = eval(fprima)
            
            xii  = xi - fxi/fprimaxi
            
            ea = abs((xii-xi)/xii)*100
            
            fila = [i+1,round(xii.real,d)+round(xii.imag,d)*1j,round(ea.real,d)]
                
            tabla.append(fila)
                
            xi = xii
                
        #print(tabulate(tabla))
        
        return round(xii.real,d)+round(xii.imag,d)*1j
        
def fractal(raices):
    
    colores =["ro","go","bo","yo","co","ko"]
    for i in arange(-2, 2,0.05):
        for k in arange(-2,2,0.05):
            
            
            zp = i+k*1j
            
            # aqui introducimos el polinomio y su derivada
            z = newtonRaphson("3*x**5 - x**3 + 2","15*x**4 - 3*x**2",zp,50,5)
            
            if abs(z-raices[0])<0.1:
                plot(i,k,colores[0])
            elif abs(z-raices[1])<0.1:
                plot(i,k,colores[1])                
            elif abs(z-raices[2])<0.1:
                plot(i,k,colores[2])
            elif abs(z-raices[3])<0.1:
                plot(i,k,colores[3])
            elif abs(z-raices[4])<0.1:
                plot(i,k,colores[4])
                
# Como llamar el fractal, esto se hace en el Puerto

# Paso 1 - Creamos un Array para Raices
# raices = []

# Paso 2 - Metemos todas las raices irreales positivas
# raices.append(newtonRaphson("ec","1era der.",2j,30,4))

# Paso 3 - Metemos todas las raices irreales negativas
# raices.append(newtonRaphson("x**3 + 1","3*x**2",-2j,30,4))

# Paso 4 - Metemos todas las raices reales
# raices.append(newtonRaphson("x**3 + 1","3*x**2",2,30,4))

# Paso 5 - Chequeamos que esten las tres raices
# raices

# Paso 6 - Introducimos la funcion...
# fractal(raices)

# HT3 - Problema 2
# Metemos todas las raices irreales positivas
# raices.append(newtonRaphson("3*x**5 - x**3 + 2","15*x**4 - 3*x**2",2j,50,4)) - POSITIVA 1
# raices.append(newtonRaphson("3*x**5 - x**3 + 2","15*x**4 - 3*x**2",1+1j,50,4)) - POSITIVA 2
# raices.append(newtonRaphson("3*x**5 - x**3 + 2","15*x**4 - 3*x**2",1-1j,50,4)) - NEGATIVA 1
# raices.append(newtonRaphson("3*x**5 - x**3 + 2","15*x**4 - 3*x**2",-2j,50,4)) - NEGATIVA 2
# raices.append(newtonRaphson("3*x**5 - x**3 + 2","15*x**4 - 3*x**2",2,50,4)) - REAL