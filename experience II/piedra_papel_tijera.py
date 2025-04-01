# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:29:44 2024

@author: ingmi
"""

print("""
      Piedra
      Papel
      Tijera
      """)

cont1 = 0
cont2 = 0
contEn = 1
Entradas = {}


while (cont1 < 2 and cont2 < 2):
    j1 = input("Jugador 1, ingrese su jugada: ").capitalize()
    j2 = input("Jugador 2, ingrese su jugada: ").capitalize()
    
    Entradas["Jugador 1"] = j1
    Entradas["Jugador 2"] = j2
    
    if (j1 == "Piedra" and j2 == "Piedra" or
        j1 == "Tijera" and j2 == "Tijera" or
        j1 == "Papel" and j2 == "Papel"):
        print("Entrada " + str(contEn) + ": " + j1 + " , " + j2)
        print("Empate")
    
    elif (j1 == "Piedra" and j2 == "Tijera" or
          j1 == "Tijera" and j2 == "Papel" or
          j1 == "Papel" and j2 == "Piedra"):
        print("Entrada " + str(contEn) + ": " + j1 + " , " + j2)
        cont1 += 1
        
    elif (j1 == "Piedra" and j2 == "Papel" or
          j1 == "Tijera" and j2 == "Piedra" or
          j1 == "Papel" and j2 == "Tijera"):
        print("Entrada " + str(contEn) + ": " + j1 + " , " + j2)
        cont2 += 1
        
    contEn += 1

if (cont1 == 2):
    print("Resultado: Ganador: Jugador 2")
else:
    print("Resultado: Ganador: Jugador 1")

# %%



