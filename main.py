import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime,date
import json


with open('databases/resources_data.json','r',encoding='utf-8') as file:
            recursos_json=json.load(file)

with open("databases/events_data.json" ,'r',encoding='utf-8') as file:
    events=json.load(file)


class app:
    def __init__(self):
        
        self.color_texto="#BCB3B8"
        self.color_fondo="#3F3D3E"
        self.color_hover="#5A575B"
        self.color_secundario="#4C4A4D"
        self.color_terciario="#8A9494"
        self.color_almost_black="#3F3D3E"
        self.color_light="#3F3D3E"
        self.color_white="#3F3D3E"
        self.color_mainborder="#524D50"

        self.principal = ctk.CTk()

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")
        
        self.principal.title("Gestor Misionero")
        self.principal.geometry("1000x650")
        self.principal.minsize(width=700,height=600)

        self.iniciar()

    def getevents(self):
        with open("databases/events_data.json",'r',encoding='utf-8') as file:
            a=json.load(file)
        return a
            
    def getres(self):
        with open('databases/resources_data.json','r',encoding='utf-8') as file:
            b=json.load(file)
        return b


    def iniciar(self):
        self.sidebar = ctk.CTkFrame(
            self.principal,
            fg_color="#3F3D3E",
            border_width=2,
            border_color=self.color_mainborder,
            corner_radius=0
        )

        self.body = ctk.CTkFrame(
            self.principal,
            fg_color="transparent",
            corner_radius=0,
            border_width=2,
            border_color=self.color_mainborder
        )   
        self.body.pack(fill="both",expand=True,side="right")

        sidebar_titulo = ctk.CTkLabel(
            self.sidebar,
            text= "Gestor Misionero",
            font=("Calibri",22,"bold"),
            text_color="#BCB3B8"
        )
        sidebar_titulo.pack(anchor="n",fill="x",pady=(7,0),padx=7)

        sidebar_subtitulo = ctk.CTkLabel(
            self.sidebar,
            text= "Que su nombre sea grande entre las naciones",
            font=("Calibri",10,"italic","bold"),
            text_color="#BCB3B8",
            wraplength=240
        )
        sidebar_subtitulo.pack(fill="x",padx=7,pady=0)

        sidebar_separador= ctk.CTkFrame(
            self.sidebar,
            height=1.5,
            fg_color="#BCB3B8",
            corner_radius=0
        )
        sidebar_separador.pack(fill="x",padx=7,pady=7,anchor="n")

        #botones

        botones_sidebar = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent",
            border_width=0,
            corner_radius=0
        )

        opciones:dict ={
            "Listar los eventos \n (o Listar para eliminar los eventos)":"listar",
            "Añadir nuevo evento":"añadir",
        }

        for opcion,llave in opciones.items():
            ctk.CTkButton(
                botones_sidebar,
                text=f"{opcion}",
                height=32,
                font=("Console", 12),
                fg_color="transparent",
                hover_color=self.color_hover,
                text_color=self.color_texto,
                border_width=1,
                border_color=self.color_terciario,
                corner_radius=0,
                command=lambda k=llave: self.mostrar(k)
            ).pack(fill="x",padx=7,pady=(8,4),ipady=1)

        
        botones_sidebar.pack(padx=8,pady=20,fill="both",expand=True)

        #"packing" la barra lateral
        self.sidebar.pack(fill="y", expand=True,anchor="w")

        self.menu_listado()

    def mostrar (self,k):
        if k=="listar":
            self.menu_listado()
        if k=="añadir":
            self.menu_añadir()    

        

    def menu_listado(self):

        for widget in self.body.winfo_children():
            widget.destroy()
    
        opcframe=ctk.CTkFrame(
            self.body,
            fg_color=self.color_white,
            corner_radius=0
        )

        #Actual entries
        self.entry1=ctk.CTkEntry(
            opcframe, 
            corner_radius=0,
            placeholder_text="Mes (1)",
            fg_color=self.color_almost_black,
            placeholder_text_color=self.color_texto,
            text_color=self.color_texto
        )
        self.entry1.pack(side="left",padx=8,pady=4)
        
        self.entry2=ctk.CTkEntry(
            opcframe, 
            corner_radius=0,
            placeholder_text="Año (2026)",
            fg_color=self.color_almost_black,
            placeholder_text_color=self.color_texto,
            text_color=self.color_texto
        )
        self.entry2.pack(side="left",padx=8,pady=4)

        self.botonlistar=ctk.CTkButton(
            opcframe,
            text="Listar",
            height=28,
            corner_radius=0,
            fg_color="transparent",
            hover_color=self.color_hover,
            text_color=self.color_texto,
            border_width=1,
            border_color=self.color_terciario,
            command=lambda k="listar": self.listar_eventos(k)
        )
        self.botonlistar.pack(side="right",padx=8,pady=4)


        self.botonlistar=ctk.CTkButton(
            opcframe,
            text="Listar para Eliminar",
            height=28,
            corner_radius=0,
            fg_color="transparent",
            hover_color=self.color_hover,
            text_color=self.color_texto,
            border_width=1,
            border_color=self.color_terciario,
            command=lambda k="eliminar": self.listar_eventos(k)
        )
        self.botonlistar.pack(side="right",padx=8,pady=4)


        self.listado = ctk.CTkScrollableFrame(
            self.body,
            height=42,
            fg_color=self.color_white,
            corner_radius=0,
            border_width=1,
            border_color=self.color_light
        )
        self.listado.pack(fill="both", expand=True, padx=14,pady=(4,10),side="bottom",ipady=10)

        opcframe.pack(fill="x",anchor="n",pady=(10,0),padx=14)

    def listar_eventos(self,modo):
        events=self.getevents().copy()
        print(events)
        pmes = self.entry1.get()
        paño=self.entry2.get()
        pmes=pmes if  pmes!= "" else "1" 
        paño=paño if paño != "" else "2026"


        try:
            for widget in self.listado.winfo_children():
                widget.destroy()

            for name,event in events[paño][pmes].items():
                ctk.CTkButton(
                    self.listado,
                    text=f"#{name}: [{event["fecha1"]} - {event["fecha2"]}] - {event["nombre"]} - {event["lugar"]}",
                    font=("Calibri",10,"italic"),
                    fg_color="transparent",
                    hover_color=self.color_terciario,
                    corner_radius=0,
                    command=lambda k=name:self.ver_detalles(k,paño,pmes,modo)
                ).pack(anchor="w",padx=7,pady=4)

        except KeyError:
            messagebox.showerror(title="Error",message="Sintaxis inválida / No hay eventos en dicho mes", icon="warning")


        except:
            print("Ocurrió algún error")


        for name,event in events[paño][pmes].items():
            print(f"--{event["nombre"]}--")
            print(f"Inicio: {event["fecha1"]}")
            print(f"Fin: {event["fecha2"]}")
            print(f"Lugar: {event["lugar"]}")

            print("Recursos:")
            for recurso in event["recursos"]:
                print(f"- {recurso}")

            print("")

            print(pmes)
            print(paño)
    
    def ver_detalles(self,k,año,mes,m):
        events=self.getevents().copy()
        b=f" Fecha Inicial: {events[año][mes][k]["fecha1"]} \n"
        b+=f" Fecha Final: {events[año][mes][k]["fecha2"]} \n"

        a="Recursos:\n"
        for recurso in events[año][mes][k]["recursos"][0]:
            a = a + f" - {recurso[0]}\nCant: {recurso[1]} \n" 

        for recurso in events[año][mes][k]["recursos"][1]:
            a = a + f" {recurso[0]}\nCant: {recurso[1]} \n"

        if m=="listar":
            messagebox.showinfo(title=f"{events[año][mes][k]["nombre"]} ({events[año][mes][k]["lugar"]}) ",message = b, detail=a)
            return
        
        c=False
        c=messagebox.askyesno(title=f"{events[año][mes][k]["nombre"]} ({events[año][mes][k]["lugar"]}) ",message = b, detail=a+"\n\nDesea Eliminar el evento?")

        if c:
            events[año]["timestamps"].pop(events[año][mes][k]["tp_index"])
            events[año]["ids"].pop(events[año]["ids"].index(k))
            events[año][mes].pop(k)
            print(events)
            with open("databases/events_data.json" ,'w',encoding='utf-8') as file:
                json.dump(events,file,indent=4,ensure_ascii=False)
            self.listar_eventos("eliminar")


            
            
        
        
            


    def menu_añadir(self):

        for widget in self.body.winfo_children():
            widget.destroy()

        # Frame para el tipo ############################################################
        
        
        self.tipo=ctk.CTkFrame(
            self.body,
            height=22,
            fg_color=self.color_fondo,
            corner_radius=0,
            border_width=1,
            border_color=self.color_light
        )
        self.tipo.pack(fill="both",padx=14,pady=(10,0),anchor="n",ipady=10)

        ###################
        #Llenando self.tipo
        ###################

        ctk.CTkLabel(
            self.tipo,
            text="Tipo de evento",
            font=("Console",14,"bold"),
        ).grid(column=1,row=1,pady=(20,0))

        opciones=["Entrega de Recursos","Donación","Taller","Conferencias"]        
        self.seleccion = ctk.StringVar(value="Entrega de Recursos")
        self.seleccion_menu = ctk.CTkOptionMenu(
            self.tipo,
            values=opciones,
            corner_radius=0,
            fg_color=self.color_almost_black,
            text_color=self.color_texto,
            dropdown_fg_color=self.color_almost_black,
            button_color=self.color_secundario,
            button_hover_color=self.color_hover,
            variable=self.seleccion,
            command=self.cambio_opcion
        ).grid(column=2,row=1,pady=(20,0))
        self.tipo.columnconfigure(1,pad=40)

        ctk.CTkButton(
            self.tipo,
            text="Validar fecha y recursos",
            height=28,
            width=28,
            corner_radius=0,
            fg_color="transparent",
            hover_color=self.color_hover,
            text_color=self.color_texto,
            border_width=1,
            border_color=self.color_terciario,
            command=self.validar_fecha
        ).grid(column=3,row=1,columnspan=2,pady=(20,0),padx=(40,0))
        self.tipo.columnconfigure(3,pad=40)

        
        

        # Formulario entrega ################################################################
        self.formulario_entrega=ctk.CTkFrame(
            self.body,
            fg_color=self.color_light,
            corner_radius=0
        )

        # Frame para los recursos ############################################################
        self.frame_recursos=ctk.CTkScrollableFrame(
            self.body,
            height=80,
            fg_color=self.color_texto,
            corner_radius=0,
            border_width=1,
            border_color=self.color_light
        )

        # Frame cambiante ############################################################
        self.cambiante=ctk.CTkFrame(
            self.body,
            height=45,
            fg_color=self.color_white,
            corner_radius=0,
            border_width=1,
            border_color=self.color_light,
        )

        #################
        #Llenando Frames
        #################
        ctk.CTkLabel(
            self.formulario_entrega,
            text="Tipo de evento",
            font=("Console",12),
        ).grid(column=1,row=1)
                
        self.pais_elegido = ctk.StringVar(value="México")
        self.seleccion_menu = ctk.CTkOptionMenu(
            self.formulario_entrega,
            values=["México","Brasil","Estados Unidos"],
            corner_radius=0,
            fg_color=self.color_almost_black,
            text_color=self.color_texto,
            dropdown_fg_color=self.color_almost_black,
            button_color=self.color_secundario,
            button_hover_color=self.color_hover,
            variable=self.pais_elegido,
            command=self.message_for_country
        ).grid(column=2,row=1) 


        #######
        #Fechas
        #######
        self.dias28 = [str(i) for i in range(1, 28)]
        self.dias29 = [str(i) for i in range(1, 29)]
        self.dias30 = [str(i) for i in range(1, 30)]
        self.dias31 = [str(i) for i in range(1, 32)]
        lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        lista_años = [str(i) for i in range(2026, 2071)]


        ctk.CTkLabel(
            self.formulario_entrega,
            text="Fecha Inicial",
            font=("Console",12),
            ).grid(column=1,row=2)

        self.dia = ctk.StringVar(value="1")
        self.seleccion_dia = ctk.CTkOptionMenu(
           self. formulario_entrega,
            values=self.dias31,
            corner_radius=0,
            fg_color=self.color_almost_black,
            text_color=self.color_texto,
            dropdown_fg_color=self.color_almost_black,
            button_color=self.color_secundario,
            dropdown_font=("Console",10),
            button_hover_color=self.color_hover,
            variable=self.dia
        ).grid(column=4,row=2)

        self.año = ctk.StringVar(value="2026")
        seleccion_año = ctk.CTkOptionMenu(
            self.formulario_entrega,
            values=lista_años,
            corner_radius=0,
            fg_color=self.color_almost_black,
            text_color=self.color_texto,
            dropdown_fg_color=self.color_almost_black,
            button_color=self.color_secundario,
            button_hover_color=self.color_hover,
            variable=self.año,
            dropdown_font=("Console",8)
        ).grid(column=2,row=2) 

        self.mes = ctk.StringVar(value="Enero")
        seleccion_mes = ctk.CTkOptionMenu(
            self.formulario_entrega,
            values=lista_meses,
            corner_radius=0,
            fg_color=self.color_almost_black,
            text_color=self.color_texto,
            dropdown_fg_color=self.color_almost_black,
            button_color=self.color_secundario,
            button_hover_color=self.color_hover,
            variable=self.mes,
            dropdown_font=("Console",10),
        ).grid(column=3,row=2)




        self.formulario_entrega.columnconfigure(1,pad=40)
        self.formulario_entrega.columnconfigure(2,pad=40)
        self.formulario_entrega.columnconfigure(3,pad=40)
        self.formulario_entrega.columnconfigure(4,pad=40)
        self.formulario_entrega.rowconfigure(1,pad=10)
        self.formulario_entrega.rowconfigure(2,pad=10)


        ctk.CTkLabel(
            self.formulario_entrega,
            text="Hora Inicial",
            font=("Console",12),
            ).grid(column=1,row=3)
        
        self.hora_elegida = ctk.StringVar(value="00:00:00")
        entryhora=ctk.CTkEntry(
            self.formulario_entrega, 
            corner_radius=0,
            placeholder_text="00:00:00",
            fg_color=self.color_almost_black,
            placeholder_text_color=self.color_texto,
            text_color=self.color_texto,
            textvariable=self.hora_elegida
        )
        entryhora.grid(column=2,row=3)

        self.formulario_entrega.rowconfigure(3,pad=20)

        ctk.CTkButton(
            self.tipo,
            text="Mostrar Recursos",
            height=28,
            width=28,
            corner_radius=0,
            fg_color="transparent",
            hover_color=self.color_hover,
            text_color=self.color_texto,
            border_width=1,
            border_color=self.color_terciario,
            command=self.mostrar_recursos
        ).grid(column=5,row=1,columnspan=2,pady=(20,0),padx=(40,0))




        self.recursos_elegidos=[[],[]]

        self.formulario_entrega.pack(fill="both", padx=14,pady=(4,0),anchor="n",ipady=10)
        #.pack(anchor="n",expand=True,fill="both")

        ##################################
        #Packing de frames y funcion final
        ##################################
        self.cambiante.pack(fill="both", padx=14,pady=(4,0),anchor="n",expand=True)
        
        self.cambio_opcion("Entrega de Recursos")

    def mostrar_recursos(self):
        for widget in self.frame_recursos.winfo_children():
            widget.destroy()

        i=1
        a=16*[1]
        for recurso,cant in recursos_json["materiales"].items():
            self.frame_recursos.columnconfigure(1,weight=10)
            a[i]=ctk.StringVar()
            ctk.CTkLabel(
                self.frame_recursos,
                text=recurso,
                text_color="#171817",
                font=("Times New Roman",15,"bold"),
            ).grid(row=i,column=1,padx=(0,0),pady=(4,0))

            ctk.CTkEntry(
                self.frame_recursos,
                width=40,
                height=10,
                placeholder_text=str(cant[0]),
                textvariable=a[i]
            ).grid(row=i,column=2,padx=(4,4),pady=(4,0))

            ctk.CTkButton(
                self.frame_recursos,
                width=20,
                height=10,
                text="Añadir a la lista",
                corner_radius=0,
                fg_color="transparent",
                hover_color="#959093",
                text_color=self.color_hover,
                border_width=1,
                border_color=self.color_terciario,
                command=lambda k=[recurso,a[i]] :self.getvalue(k)
            ).grid(row=i,column=3,pady=(4,0),padx=(0,30))
            i+=1
        self.frame_recursos.pack(fill="both", expand=True, padx=14,pady=(4,17),anchor="n",ipady=20)


    
    def cambio_opcion(self,opcion):
        self.evento_elegido=opcion
        #Se mantienen las fechas y lo elegido en el frame de opciones pq igual sirven para estos eventos
        if opcion=="Entrega de Recursos":
            self.mostrar_entrega()
        if opcion=="Conferencias":
            self.mostrar_conferencias()

    def mostrar_entrega(self):
        for widget in self.cambiante.winfo_children():
            widget.destroy()

        self.titulo_fecha2=ctk.CTkLabel(self.cambiante, text="Fecha y hora finales")
        self.label_fecha2=ctk.CTkLabel(self.cambiante)

    def mostrar_conferencias(self):
        pass


        

    def getvalue(self,e):

        
        for i,elemento in enumerate(self.recursos_elegidos[0]):
            print(elemento[0])

            if elemento[0] == e[0]:
                try:
                    if ((e[1].get()).strip()=="") or (e[1].get()).strip() == "0" :
                        #cambio aqui
                        self.recursos_elegidos[0].pop(i)
                        print(self.recursos_elegidos)
                        x=""
                        y=""
                        for e in self.recursos_elegidos[0]:
                            x= x + e[0] + ": " + str(e[1])  + "\n"
                        for e in self.recursos_elegidos[1]:
                            y = y + e[0] +": "+ "\n"

                        if x!="":
                            x = "Recursos materiales elegidos:\n" + x
                        if y!="":
                            y = "\nPersonal elegido:" + y

                        messagebox.showinfo(message=x + y)
                        return
                    else:
                        self.recursos_elegidos[0][i][1]=int(e[1].get())
                        print(self.recursos_elegidos)

                        x=""
                        y=""
                        for e in self.recursos_elegidos[0]:
                            x= x + e[0] + ": " + str(e[1])  + "\n"
                        for e in self.recursos_elegidos[1]:
                            y = y + e[0] +": "+ "\n"

                        if x!="":
                            x = "Recursos materiales elegidos:\n" + x
                        if y!="":
                            y = "\nPersonal elegido:" + y

                        messagebox.showinfo(message=x + y)
                        return
                except:
                    print(self.recursos_elegidos)
                    messagebox.showwarning(message="Probablemente hay un error de sintaxis en la cantidad de recursos")
                    return

        

        try:
            if(int(e[1].get()) <= recursos_json["materiales"][e[0]][0]):
                self.recursos_elegidos[0].append([e[0],int(e[1].get())])
                print(self.recursos_elegidos)
                x=""
                y=""
                for e in self.recursos_elegidos[0]:
                    x= x + e[0] + ": " + str(e[1])  + "\n"
                for e in self.recursos_elegidos[1]:
                    y = y + e[0] +": "+ "\n"

                if y!="":
                    y = "\nPersonal elegido:" + y

                messagebox.showinfo(message="Recursos materiales elegidos:\n" + x + y)
            else:
                messagebox.showwarning(message="Probablemente hay un error en la cantidad de recursos")    
        except:
            print(self.recursos_elegidos)
            messagebox.showwarning(message="Probablemente hay un error de sintaxis en la cantidad de recursos")

    def message_for_country(self,cty):
        tiempo={
            "México":7,
            "Brasil":10,
            "Estados Unidos":5
            }
        messagebox.showinfo(message=f"Las entregas a {cty} se tardan {tiempo[cty]} días")

    def validar_fecha(self):
        if (len(self.recursos_elegidos[0])==0) and (len(self.recursos_elegidos[1])==0):
            messagebox.showerror(message="Tiene que seleccionar almenos un recurso")
            return
        
        meses_dict = {
            "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
            "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
            "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
        }
        y=int(self.año.get())
        m=meses_dict[self.mes.get()]
        d=int(self.dia.get())
        aña=True
        eñe=True


        if not(y%400==0 or (y%4==0 and y%100!=0)) and m==2 and d>28:
            aña= False
            eñe= False

        
        if (y%400==0 or (y%4==0 and y%100!=0)) and m==2 and d>29:
            aña= False
        
        if (m==4 or m==6 or m==9 or m==11) and d==31:
            eñe= False
        
        if aña == True and eñe == True:
            self.validar_hora(y,m,d)
        elif aña == False and eñe==False:
            messagebox.showwarning(message="Febrero no tiene más de 28 días")
        elif eñe==False:
            messagebox.showwarning(message="Este mes no tiene 31 días")
        elif aña==False:
            messagebox.showwarning(message="Febrero no tiene más de 29 días en años bisiestos")


        


    def validar_hora(self,y,m,d):

        
            hg=self.hora_elegida.get()
            hg=hg.strip()
            #hg = self.hora_elegida.get()

            if hg[2]==":" and hg[5]==":":
                hg=hg.split(":")
                try:
                    h=int(hg[0]) if hg[0][0]!="0" else int(hg[0][1]) 
                    min=int(hg[1]) if hg[1][0]!="0" else int(hg[1][1])
                    s=int(hg[2]) if hg[2][0]!="0" else int(hg[2][1])
                except:
                    messagebox.showerror(message="Sintaxis Inválida para la hora")
                    return

                try:
                    self.fecha1=datetime(y,m,d,h,min,s)
                    print("Fecha Añadida con éxito")
                except ValueError as e:
                    messagebox.showerror(message=str(e))
                    return


            tiempo={
            "México":7,
            "Brasil":10,
            "Estados Unidos":5
            }
            self.fecha2 = self.fecha1+(datetime(2026,1,tiempo[self.pais_elegido.get()]+1)-datetime(2026,1,1))

            self.titulo_fecha2.pack_forget()
            self.label_fecha2.pack_forget()
            
            self.titulo_fecha2.configure(text="Fecha y hora finales")
            self.label_fecha2.configure(text=self.fecha2.strftime("%Y-%m-%d %H:%M:%S"))
            messagebox.showinfo(message=f"Fecha Final: {self.fecha2.strftime("%d-%m-%y %H:%M:%S")}")

            self.titulo_fecha2.pack(side="left",padx=(65,20))
            self.label_fecha2.pack(side="left")
            

            self.validar_recursos()


        
    def validar_recursos(self):
        events=self.getevents().copy()
        recursos_json=self.getres().copy()
    
        try:
            error_depends={
                "México":["Material de Capacitación Evangelística (Español)","Material de Capacitación Pastoral (Español)","Material de Capacitación Ministerial (Español)"],
                "Brasil":["Material de Capacitación Evangelística (Portugués)","Material de Capacitación Pastoral (Portugués)","Material de Capacitación Ministerial (Portugués)"],
                "Estados Unidos":["Material de Capacitación Evangelística (Inglés)","Material de Capacitación Pastoral (Inglés)","Material de Capacitación Ministerial (Inglés)"]
            }
            error_pais={
                "México":["Material de Capacitación Evangelística (Portugués)","Material de Capacitación Pastoral (Portugués)","Material de Capacitación Ministerial (Portugués)",            "Biblias en Portugués (Cajas)",
            "Tratados Evangelísticos en Portugués"
                            "Material de Capacitación Evangelística (Inglés)","Material de Capacitación Pastoral (Inglés)","Material de Capacitación Ministerial (Inglés)",            "Biblias en Inglés (Cajas)",
            "Tratados Evangelísticos en Inglés",],
                "Brasil":["Material de Capacitación Evangelística (Español)","Material de Capacitación Pastoral (Español)","Material de Capacitación Ministerial (Español)",            "Biblias en Español (Cajas)",
            "Tratados Evangelísticos en Español",
                          "Material de Capacitación Evangelística (Inglés)","Material de Capacitación Pastoral (Inglés)","Material de Capacitación Ministerial (Inglés)",            "Biblias en Inglés (Cajas)",
            "Tratados Evangelísticos en Inglés",],

                "Estados Unidos":["Material de Capacitación Evangelística (Español)","Material de Capacitación Pastoral (Español)","Material de Capacitación Ministerial (Español)",            "Biblias en Español (Cajas)",
            "Tratados Evangelísticos en Español",
                                  "Material de Capacitación Evangelística (Portugués)","Material de Capacitación Pastoral (Portugués)","Material de Capacitación Ministerial (Portugués)",            "Biblias en Portugués (Cajas)",
            "Tratados Evangelísticos en Portugués"]
            }

            idioma={
                "México":"Español",
                "Brasil":"Portugués",
                "Estados Unidos":"Inglés"
            }

            bit1=False
            bit2=False

            for elem in self.recursos_elegidos[0]:
                if elem[0] in error_pais[self.pais_elegido.get()]:
                    messagebox.showwarning(message=f"Los recursos deben de estar acorde al idioma hablado en el pais ( País Elegido:{self.pais_elegido.get()} - Idioma:{idioma[self.pais_elegido.get()]}.)")
                    return
                if elem[0]==error_depends[self.pais_elegido.get()][0] or elem[0]==error_depends[self.pais_elegido.get()][1]:
                    bit1=True
                if elem[0]==error_depends[self.pais_elegido.get()][2]:
                    bit2=True
                
            if bit1 and not(bit2):
                messagebox.showwarning(message="El Material de Capacitación Evangelística y/o el Pastoral necesitan ser enviados junto con el ministerial ")
                return
            

            messagebox.showinfo(message="Recursos Válidos")
                    
            

        except ValueError as e:
            input(e)

    
#me falta añadir la diferenc

        resources=recursos_json.copy()
        print(f"Lista bruta: {resources}")

        fecha=[self.fecha1,self.fecha2]
        
        
        def remove(tp):
            for recurso in tp[0]:
                resources["materiales"][recurso[0]][0]-= recurso[1]

            for recurso in tp[1]:
                resources["humanos"][recurso[0]]-= recurso[1]


        
        for tp in events[str(fecha[1].year)]["timestamps"]:
            a=datetime.strptime(tp[0],"%Y-%m-%d %H:%M:%S")
            b=datetime.strptime(tp[1],"%Y-%m-%d %H:%M:%S")
        if (len(events[str(fecha[1].year)]["timestamps"])!=0) and (fecha[0]<=a and a<=fecha[1]) or (fecha[0]<=b and b<=fecha[1]) or (a<=fecha[0] and fecha[1]<=b):
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
        

        for recurso in self.recursos_elegidos[0]:
            print(f"\n\nLista procesada: {resources}\n")
            if(resources["materiales"][recurso[0]][0]- recurso[1]) < 0:
                messagebox.showerror(message=f"No hay suficientes {recurso[0]} para planificar el evento")
                return


        for recurso in self.recursos_elegidos[1]:
            if (resources["humanos"][recurso[0]]- recurso[1]) < 0:
                messagebox.showerror(message=f"No hay suficientes {recurso[0]} para planificar el evento")
                return

        messagebox.showinfo(message="Suficientes recursos en el tiempo solicitado para planificar el evento")
        a = messagebox.askyesno(message="¿Desea añadir ya el evento a la base de datos?",detail="Si selecciona \"No\" tendra que pasar por la validación de nuevo para añadir el evento")
        if a: self.añadir_al_json()
              
    def añadir_al_json(self):
        self.getevents()
        self.getres()
        #Manejo de ID
        id=str(events["idcount"])
        events["idcount"]+=1
        y=str(self.fecha1.year)
        m=str(self.fecha1.month)
    
        #Añadir el evento al json
        events[y][m][id]={}
        events[y][m][id]["nombre"]=self.evento_elegido
        events[y][m][id]["fecha1"]=self.fecha1.strftime("%Y-%m-%d %H:%M:%S")
        events[y][m][id]["fecha2"]=self.fecha2.strftime("%Y-%m-%d %H:%M:%S")
        events[y][m][id]["lugar"]=self.pais_elegido.get()
        events[y][m][id]["recursos"]=self.recursos_elegidos
        events[y][m][id]["tp_index"]=len(events[y]["timestamps"])

        #Añadir a id's del año
        events[y]["ids"].append(id)
        #Añadir Timestamp
        
        events[y]["timestamps"].append([self.fecha1.strftime("%Y-%m-%d %H:%M:%S"),self.fecha2.strftime("%Y-%m-%d %H:%M:%S"),self.recursos_elegidos])
            

        with open("databases/events_data.json" ,'w',encoding='utf-8') as file:
            json.dump(events,file,indent=4,ensure_ascii=False)
        
        self.recursos_elegidos=[[],[]]
        

        




    def ejecutar(self):
        self.principal.mainloop()
    

if __name__ == "__main__":

    print("Iniciando el Gestor")

    app = app()
    app.ejecutar()
