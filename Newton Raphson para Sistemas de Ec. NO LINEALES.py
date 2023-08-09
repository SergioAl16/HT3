# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
20/07/2023

Metodo de Newton Raphson para Sistemas de Ec. NO LINEALES (2x2)
"""

from pylab import *
from tabulate import tabulate

def newtonRaphson(u,v,ux,uy,vx,vy,x0,y0,n,d):
    
    #xi = float(x0)
    
    xi = x0
    yi = y0
    
    tabla = [['i','xi','yi','eax','eay'],[0,xi,yi]]
    
    for i in range(n):
    
        x = xi
        y = yi
    
        ui = eval(u)
        vi = eval(v)
        
        uxi = eval(ux)
        vxi = eval(vx)
    
        uyi = eval(uy)
        vyi = eval(vy)
    
        j = uxi*vyi - uyi*vxi
        
        xii = xi - ((ui*vyi - vi*uyi)/j)
        yii = yi - ((vi*uxi - ui*vxi)/j)
        
        eax = abs((xii-xi)/xii)*100
        eay = abs((yii-yi)/yii)*100
        
        fila = [i+1,round(xii.real,d)+round(xii.imag,d)*1j,round(yii.real,d)+round(yii.imag,d)*1j,round(eay.real,d),round(eax.real,d)]
        
        tabla.append(fila)
    
        xi = xii
        yi = yii
    
    print(tabulate(tabla))

# newtonRaphson("FUNC X", "FUNC Y","DERV XX","DERV XY","DERV YX","DERV YY",1-1j,1-1j,10,5)    

# EJERCICIO EN CLASE
# newtonRaphson("x**2+y**2-1", "(x-2)**2+(y-1)**2-1","2*x","2*y","2*(x-2)","2*(y-1)",1-1j,1-1j,10,5)

# HT3 - PROBLEMA 3
# newtonRaphson("0.75 + x - x**2", "x**2 - y - 5*x*y", "1 - 2*x", "-1", "-5*y", "2*x - 1", -0.1868 + 0.5283j, 0.2395 + 1.3721j, 10000, 4)
# newtonRaphson("x**2 + 1 - y", "2*cos(x) - y", "-2*x", "-1", "-2*sin(x)", "-1", -0.715 + 1.511j, 1.511 + 0.715j, 10, 4)
# newtonRaphson("(x - 4)**2 + (y - 4)**2 - 5", "x**2 + y**2 - 16", "2*(x - 4)", "2*(y - 4)", "2*x", "2*y", 1.806 + 3.569j, 3.569 + 1.806j, 10, 5)

