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
                
        print(tabulate(tabla))
        
# Primer Ejercicio en Clase    
# newtonRaphson("x**6+x**5+2*x**4-5*x**3+x**2+x-1", "6*x**5+5*x**4+8*x**3-15*x**2+2*x+1",2j,30,4)

# Segundo Ejercicio en Clase
# newtonRaphson("e**x+1","e**x", 2j,30,4)

# Tercer Ejercicio en Clase
# newtonRaphson("cos(x)-5", "-sin(x)",2j,30,4)

# Cuarto Ejercicio en Clase Fractal
# newtonRaphson("x**3 + 1","3*x**2",2j,30,4)

# HT - Problema 1
# newtonRaphson("e**x + 4","e**x",1+2j,15,4)
# newtonRaphson("e**x + 4","e**x",1+1j,15,4)
# newtonRaphson("e**x + 4","e**x",1-1j,15,4)
# newtonRaphson("e**x + 4","e**x",1-2j,15,4)