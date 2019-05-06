#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:11:30 2018

@author: clarissa
"""
# Plotting Ulam's Spiral

print('Defina a dimensão da lateral do quadrado:')
l = int(input('>'))
l_2 = l**2
seq = range(1, l_2)
x, y = 0, 0

# definindo coordenadas dos pontos

quadrados = [x, y]
repeticoes_1 = 0
repeticoes_2 = 0
teste_se_impar = 0

for i in range(2, l+1):
    teste_se_impar = i
    if not teste_se_impar % 2: #if Verdadeiro = Par
        x += 1
        y += 0
    else:                    #if Falso = Impar
        x -= 1
        y += 0
    quadrados.append(x)
    quadrados.append(y)


    repeticoes_1 = i - 1
    repeticoes_2 = i - 1
    while repeticoes_1 > 0:
        if not teste_se_impar % 2: #if Verdadeiro = Par
            x -= 0
            y += 1
        else:                    #if Falso = Impar
            x += 0
            y -= 1
        quadrados.append(x)
        quadrados.append(y)
        repeticoes_1 = repeticoes_1 - 1
        
    while repeticoes_2 > 0:
        if not teste_se_impar % 2: #if Verdadeiro = Par
            x -= 1
            y -= 0
        else:                    #if Falso = Impar
            x += 1
            y -= 0
        quadrados.append(x)
        quadrados.append(y)
        repeticoes_2 = repeticoes_2 - 1        

# assinalando um numero a um par de coordenadas
pontos_x = quadrados[::2]
pontos_y = quadrados[1::2]

# definindo um teste de primalidade

import math

def prmlty(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# testando nossos primos
x_primo = []
y_primo = []
    
for i in range(1,l_2-1):
    if prmlty(i):
        x_primo.append(pontos_x[i])
        y_primo.append(pontos_y[i])

        
import matplotlib.pyplot as plt

plt.plot(x_primo, y_primo, 'b.')
plt.show()
























