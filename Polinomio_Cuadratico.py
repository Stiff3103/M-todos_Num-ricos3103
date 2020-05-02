# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:13:17 2020

@author: Stiff
"""
print('''Hola, 
el siguiente programa funciona como un ejercicio de interpolación cuadratica,
es decir funciona para encontrar los valores de Fx, dado el valor de x''')



def Polinomio_Cuadratico(x,fx):
    f0=fx[0]
    f1=(fx[0]-fx[1])/(x[1]-x[0])
    f2=(((fx[2]-fx[1])/(x[2]-x[1]))-((fx[1]-fx[0])-(x[1]-x[0])))/(x[2]-x[0])
    formulaCuadratica=f0+f1*(x[3]-x[0])+f2*(x[3]-x[0])*(x[3]-x[1])
    return(formulaCuadratica)
x=[ ]
fx=[ ]
print('Este sistema de interpolación')
for i in range(0,3):
    xx=float(input('ingrese el valor de x['+str(i+1)+'] '))
    x.append(xx)
    fxx=float(input('ingrese el valor de fx['+str(i+1)+'] '))
    fx.append(fxx)
xx=float(input('Valor para calcular x1: '))
x.append(xx)
print('las coordenadas son: ', Polinomio_Cuadratico(x,fx))
    
