# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:10:10 2020

@author: Stiff
"""
print('''
            Programa Runge Kutta diseñado para encontrar soluciones 
            a problemas de ecuaciones diferenciales de cuarto orden
 Donde:
     a y b es un intervalo y:
         a es el inicio de la grafica con respecto al eje x
         b es el fin de la grafica con respecto al eje x
     y0 es la condición inicial
     h es una pendiente estimada   
''') 

import numpy
import matplotlib.pyplot as plt

def f(x,y):
    return x**2-3*y
def RungeKutta(f,a,b,y0,h):
    x= numpy.arange(a,b+h,h)
    n=len(x)
    y=numpy.zeros(n)
    y[0]=y0
    contador=0
    for i in range(0,n-1):
        contador+=1
        k1=f(x[i],y[i])
        k2=f(x[i]+h/2,y[i]+k1*h/2)
        k3=f(x[i]+h/2,y[i]+k2*h/2)
        k4=f(x[i]+h,y[i]+k3*h)
        y[i+1]=y[i]+(h/6)*(k1+2*k2+2*k3+k4)
        print('La iteración ',contador,' es igual a: ', y[i+1])
    plt.plot(x,y)
    plt.show()
    
    
a=float(input('Inserte el valor de a: '))
b=float(input('Inserte el valor de b: '))
y0=float(input('Inserte el valor de y0: '))
h=float(input('Inserte el valor de h: '))

RungeKutta(f, a, b, y0, h) 


