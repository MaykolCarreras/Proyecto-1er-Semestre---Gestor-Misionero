import json
import time
import os
from datetime import datetime,date

with open("databases/events_data.json" ,'r',encoding='utf-8') as file:
        events=json.load(file)

def limp():
    os.system('cls' if os.name == 'nt' else 'clear')

#####################
#Bloque Listar Evento
#####################

def elegir_fecha():
    while True:
        limp()
        print("Elige la fecha en la que quieres ver los eventos:")
        year = input("Año: ")
        month = input("Mes: ")
        if year in events.keys() and month in events[year].keys():
            listarEventos(year,month)
            break
        else:
            print("No hay evenos en dicho año o mes, intente de nuevo")
            input()

def listarEventos(year,month): 
    limp()
    for name,event in events[year][month].items():
        print(f"--{event["nombre"]}--")
        print(f"Inicio: {event["fecha1"]}")
        print(f"Fin: {event["fecha2"]}")
        print(f"Lugar: {event["lugar"]}")

        print("Recursos:")
        for recurso in event["recursos"]:
            print(f"- {recurso}")

        print("")
    return    


#######################
#Bloque Listar Personal
#######################

def listarPersonal(): 
    with open('databases/human_res_data.json','r',encoding='utf-8') as file:
        events=json.load(file)
        
    print("--Personal Disponible--")
    print("")
    for name,cant in events.items():
        print(f"{name}: {cant}")


#######################
#Bloque Listar Recursos
#######################

def listarRecursos(): 
    with open('databases/resources_data.json','r',encoding='utf-8') as file:
        events=json.load(file)
        
    print("--Recursos Disponibles--")
    print("")
    for name,cant in events.items():
        print(f"{name}: {cant}")


#####################
#Bloque Añadir Evento
#####################


#################Validadores de fecha##########################################################################

def fecha_puntual(opcion,pais):
    Especificaciones={
    "1":
    {
    "1": "Las entregas a México duran 7 días",
    "2": "Las entregas a Brasil duran 10 días",
    "3": "Las entregas a Estados Unidos duran 5 días"
    },

    "2":"Las doncaiones son hechas en 4 horas, pero no se pueden iniciar actividades al mismo tiempo",

    "4":"Las conferencias deben de durar mínimo 1 día y máximo 3 semanas",
    }

    tiempo={
    "1":7,
    "2":10,
    "3":5
    }

    while True:
        limp()
        print("             [AVISO PREDETERMINADO]")
        print(" Al poner un mes/dia/hora etc. de un solo dígito,")
        input(" es necesario que se ingrese en el formato 1, no 01")
        
        limp()

        print("[Especificaciones]")
        try:
            print(Especificaciones[opcion][pais])

        except:
            print(Especificaciones[opcion])

        print()

        print("Elija la fecha y hora iniciales ():")
        a=int(input("El año (YYYY): "))
        m=int(input("El mes (MM): "))
        d=int(input("El día (DD): "))
        h=int(input("La hora (hh):"))
        min=int(input("El minuto (mm):"))
        s=int(input("El segundo (ss):"))

        try:
            fecha1 = datetime(a,m,d,h,min,s)
            print(fecha1)
        except ValueError as e:
            print()
            print("Ocurrio un error:")
            print(f"====> {e}__")
            print()
            input("Presione una tecla para volver a intentar")
            continue
        
        limp()

        if opcion=="4":
            print("Elija la fecha y hora finales:")
            a2=int(input("El año (YYYY): "))
            m2=int(input("El mes (MM): "))
            d2=int(input("El día (DD): "))
            h2=int(input("La hora (hh):"))
            min2=int(input("El minuto (mm):"))
            s2=int(input("El segundo (ss):"))

            try:
                fecha2 = datetime(a2,m2,d2,h2,min2,s2)
                print(fecha2)
            except ValueError as e:
                print()
                print("Ocurrio un error:")
                print(f"====> {e}")
                print()
                input("Presione una tecla para volver a intentar ")
                continue
            
            dif = fecha2 - fecha1
            
            difsec=dif.total_seconds()

            if difsec<86400:
                limp()
                print(f"Tu fecha inicial: {fecha1}")
                print(f"Tu fecha final: {fecha2}")
                print()
                if difsec<0:
                    print("Asegurese de que las fechas inicial y final no esten intercambiadas")
                else:
                    print("Las conferencias tienen que durar como mínimo 1 día")

                print()
                input("Toque una tecla para volver a intentar ")
                continue

            if dif.total_seconds()>604800:
                limp()
                print(f"Tu fecha inicial: {fecha1}")
                print(f"Tu fecha final: {fecha2}")
                print()
                print("Las conferencias no pueden durar mas de 7 días")

                print()
                input("Toque una tecla para continuar")
                continue

        elif opcion=="2":#########################OPTIMIZAR
            fecha2 = fecha1+(datetime(2026,1,1,4+1)-datetime(2026,1,1,1))
            print(datetime(2026,1,1,4+1)-datetime(2026,1,1,1))

        elif opcion=="1":
            a=tiempo[pais]
            fecha2 = fecha1+(datetime(2026,1,tiempo[pais]+1)-datetime(2026,1,1))
            input(datetime(2026,1,tiempo[pais]+1)-datetime(2026,1,1))
        
        return [fecha1,fecha2]
    

def fecha_serie():
    limp()
    print("Todavía por desarrollar")
    return


#################Validadores de recursos#######################################################################
def selecc_recursos(opcion,pais,fecha):

    with open('databases/resources_data.json','r',encoding='utf-8') as file:
        resources=json.load(file)

    if opcion == "1":
        
        while True:
            limp()
            i=1
            print("Seleccione los recursos a donar (ID - Cantidad):")
            for recurso,cantidad in resources["materiales"].items():
                print(f"{i}. {recurso}: {cantidad[0]}")
                i+=1
            print()

            rec1=[]
            cant1=[]

            j=1

            print("Escribe [salir] para salir")##########################Peligroso aquí
            while True:
                aux1=input(f"Tu elección número {j}: ")
                try:
                    if aux1=="salir":
                        break
                    aux1 = aux1.strip()
                    aux1 = aux1.split("-")
                    aux = [a.strip() for a in aux1]
                    rec1.append(aux[0])
                    cant1.append(int(aux[1]))
                    j+=1
                except:
                    rec1.pop()
                    print("Error de Sintaxis")
            
            limp()
            print(rec1)
            print(cant1)

            try:
                error_depends={
                    "1":["1","2","3"],
                    "2":["4","5","6"],
                    "3":["7","8","9"]
                }
                error_pais={
                    "1":["4","5","6","7","8","9"],
                    "2":["1","2","3","7","8","9"],
                    "3":["1","2","3","4","5","6"]
                }

                for elem in rec1:
                    if elem in error_pais[pais]:
                        input("[AVISO]") 
                        input(f"Los recursos deben de estar acorde al idioma hablado en el pais ( Tu elección: {pais}.)")
                        continue

                if (error_depends[pais][0] in rec1 or error_depends[pais][1] in rec1) and (not(error_depends[pais][2] in rec1)):
                    input("[AVISO]") 
                    input("El Material de Capacitación Evangelística y/o el Pastoral necesitan ser enviados junto con el ministerial ")
                    continue

                if chequeo(rec1,cant1,[],[],fecha):
                    
                    return[rec1,cant1,[],[]]

            except ValueError as e:
                limp()
                input(e)
                continue
#me falta añadir la diferenciacion entre cand 1 cand 2 y demas pero biem

    if opcion == "4":
        pass


def chequeo(rec,cant1,hum,cant2,fecha):

    cand=[rec,hum]

    with open('databases/resources_data.json','r',encoding='utf-8') as file:
        resources=json.load(file)

    def remove(tp):

        for recurso in tp[0]:
            resources["materiales"][recurso[0]]= resources["materiales"][recurso[0]] - recurso[1]
        
        for recurso in tp[1]:
            resources["humanos"][recurso[0]]= resources["humanos"][recurso[0]] - recurso[1]
        

    
    for tp in events[str(fecha[1].year)]["timestamps"]:
        a=datetime.strptime(tp[0],"%Y-%m-%d %H:%M:%S")
        b=datetime.strptime(tp[1],"%Y-%m-%d %H:%M:%S")
        
        if (fecha[0]<=a and a<=fecha[1]) or (fecha[0]<=b and b<=fecha[1]) or (a<=fecha[0] and fecha[1]<=b):
            remove(tp[2])

    dictaux={
    "1":"Material de Capacitación Evangelística (Español)",
    "2":"Material de Capacitación Pastoral (Español)",
    "3":"Material de Capacitación Ministerial (Español)",
    "4":"Material de Capacitación Evangelística (Portugués)",
    "5":"Material de Capacitación Pastoral (Portugués)",
    "6":"Material de Capacitación Ministerial (Portugués)",
    "7":"Material de Capacitación Evangelística (Inglés)",
    "8":"Material de Capacitación Pastoral (Inglés)",
    "9":"Material de Capacitación Ministerial (Inglés)",
    "10":"Biblias en Español (Cajas)",
    "11":"Biblias en Portugués (Cajas)",
    "12":"Biblias en Inglés (Cajas)",
    "13":"Tratados Evangelísticos en Español",
    "14":"Tratados Evangelísticos en Inglés",
    "15":"Tratados Evangelísticos en Portugués"
    }
    
    for i in range(len(rec)):

        print(rec[i])
        print(dictaux[rec[i]])
        print(dictaux)
        input()
        print(resources["materiales"][dictaux[rec[i]]])
        resources["materiales"][dictaux[rec[i]]][0] -= cant1[i]
        if (resources["materiales"][dictaux[rec[i]]][0]) < 0:
            print(f"No hay suficientes: {rec[i]} para organizar el evento.")
            input()
            return False

    #for i in range(len(hum)):
    #    resources["humanos"][hum[i]] -= cant2[i]
    #    if (resources["humanos"][hum[i]]) < 0:
    #        print(f"{rec[i]} no se encuentra disponible para organizar el evento.")
    #        input()
    #        return False
        

    return True
    

#################-------Añadir Evento (Principal)-------#######################################################
def añadir_evento():
    opcionval=["","Entrega de recursos","Donacion","Taller","Conferencias"]
    
    while True:
        
        limp()
        print("Elige el tipo de evento/acción:")
        print("1. Entrega de recursos")
        print("2. Donacion")
        print("3. Taller")
        print("4. Conferencia(s)")
        print("Escribe [salir] para, adivina qué, ¡exacto! Para salir.")

        opcion = input("Su opción (#): ")

        #####################
        #Bloque de validación
        #####################

        if opcion.lower()=="salir":
            input("Nos vemos")
            return
        if opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4":
            limp()
            for a in range(1,4):
                print("\rOpcion Incorrecta"+a*".", end="")
                time.sleep(0.7)
            continue

        if opcion=="3" or opcion=="2": 
            print("La opción de los talleres está aun en desarrollo")
            continue


        ##################
        #Selección de país
        ##################

        while True:
            limp()
            print("Elige el país deseado para el evento/acción: ")
            print("1. México")
            print("2. Brasil")
            print("3. Estados Unidos")
            print("Escriba [salir] para salir")
            print()
            pais=input("Su opción (#): ")

            if pais=="1" or pais=="2" or pais=="3":
                break

            else:
                limp()
                for a in range(1,4):
                    print("\rOpción Incorrecta"+a*".", end="")
                    time.sleep(0.7)
                continue

        #################
        #Una vez validado
        #################

        #Unused
        #if opcion=="3":
        #    fecha_serie()
        #    break

        nombre_eventos={
            "1":"Entrega de Recursos",
            "2":"Donación",
            "3":"Taller",
            "4":"Conferencia",
        }
        nombre_paises={
            "1":"Mexico",
            "2":"Brasil",
            "3":"Estados Unidos"
        }

        evento={}

        fecha = fecha_puntual(opcion,pais)
        evento["nombre"]=nombre_eventos[opcion]
        evento["fecha1"]=fecha[0].strftime("%Y-%m-%d %H:%M:%S")
        evento["fecha2"]=fecha[1].strftime("%Y-%m-%d %H:%M:%S")
        evento["lugar"]=nombre_paises[pais]

        res = selecc_recursos(opcion,pais,fecha)
        aux=[[],[]]

        #return[rec1,cant1,[],[]]
        dictaux={
        "1":"Material de Capacitación Evangelística (Español)",
        "2":"Material de Capacitación Pastoral (Español)",
        "3":"Material de Capacitación Ministerial (Español)",
        "4":"Material de Capacitación Evangelística (Portugués)",
        "5":"Material de Capacitación Pastoral (Portugués)",
        "6":"Material de Capacitación Ministerial (Portugués)",
        "7":"Material de Capacitación Evangelística (Inglés)",
        "8":"Material de Capacitación Pastoral (Inglés)",
        "9":"Material de Capacitación Ministerial (Inglés)",
        "10":"Biblias en Español (Cajas)",
        "11":"Biblias en Portugués (Cajas)",
        "12":"Biblias en Inglés (Cajas)",
        "13":"Tratados Evangelísticos en Español",
        "14":"Tratados Evangelísticos en Inglés",
        "15":"Tratados Evangelísticos en Portugués"
        }

        for i in range(len(res[0])):
            res[0][i] = dictaux[res[0][i]]

        for i in range(len(res[2])):
            res[2][i] = dictaux[res[2][i]]

        for i in range(len(res[0])):
            aux[0].append([res[0][i],res[1][i]])

        for i in range(len(res[2])):
            aux[1].append([res[2][i],res[3][i]])

        evento["recursos"]=aux

        limp()

        print(evento)

        input()
        eventoaux={}
        eventoaux[str(events["idcount"])]=evento
        events["idcount"]+=1

        limp()
        events[str(fecha[0].year)][str(fecha[0].month)].update(eventoaux)
        aux2=[evento["fecha1"],evento["fecha2"],evento["recursos"]]
        events[str(fecha[0].year)]["timestamps"].append(aux2)

        print(events)

        input()

        break