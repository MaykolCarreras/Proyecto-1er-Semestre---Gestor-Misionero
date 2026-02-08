import os
import time
from functions_dump import *
#listarEventos,listarPersonal,listarRecursos

def limp():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limp()
    print("Bienvenido a la terminal de gestión de Heartcry")
    print("1. Listar Eventos") # done
    print("2. Ver personal disponible")
    print("3. Ver recursos disponibles")
    print("4. Agregar Evento")
    print("5. Agregar Evento en Serie")
    print("6. Eliminar Evento")
    print("7. Eliminar Evento en Serie")
    print("Escribe [salir] para...bueno, para salir.")

    opcion=input("Elige una Opción (#): ")

    if opcion=="1":
        limp()
        elegir_fecha()
        input()

    elif opcion=="2":
        limp()
        listarPersonal()
        input()

    elif opcion=="3":
        limp()
        listarRecursos()
        input()

    elif opcion=="4":
        añadir_evento()
        limp()

    elif opcion=="5":
        limp()

    elif opcion=="6":
        limp()

    elif opcion=="7":
        limp()
    
    elif opcion.lower()=="salir":
        limp()
        for a in range(1,4):
            print("\rGracias por usar este programa, saliendo"+a*".", end="")
            time.sleep(0.7)
        limp()
        break
    
    else:
        limp()
        for a in range(1,4):
            print("\rCargando"+a*".", end="")
            time.sleep(0.7)

        continue

