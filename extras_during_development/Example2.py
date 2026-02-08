import customtkinter as ctk
from datetime import datetime
import calendar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.title("Selector de Fechas - Aplicación Completa")
        self.geometry("500x600")
        
        # Configurar tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Marco principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Título
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="📅 SELECTOR DE FECHAS", 
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=(20, 30))
        
        # Frame para fecha
        self.date_frame = ctk.CTkFrame(self.main_frame)
        self.date_frame.pack(pady=10, padx=20, fill="x")
        
        # Listas para días, meses y años
        self.dias = [str(i) for i in range(1, 32)]
        self.meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        self.años = [str(i) for i in range(2000, 2031)]
        
        # Variables para los dropdowns
        self.dia_var = ctk.StringVar(value="1")
        self.mes_var = ctk.StringVar(value="Enero")
        self.año_var = ctk.StringVar(value="2024")
        
        # Día
        ctk.CTkLabel(self.date_frame, text="Día:", font=("Arial", 14)).pack(pady=(10, 5))
        self.dia_menu = ctk.CTkOptionMenu(
            self.date_frame, 
            values=self.dias, 
            variable=self.dia_var,
            font=("Arial", 14),
            width=200,
            command=self.validar_fecha
        )
        self.dia_menu.pack(pady=5)
        
        # Mes
        ctk.CTkLabel(self.date_frame, text="Mes:", font=("Arial", 14)).pack(pady=(10, 5))
        self.mes_menu = ctk.CTkOptionMenu(
            self.date_frame, 
            values=self.meses, 
            variable=self.mes_var,
            font=("Arial", 14),
            width=200,
            command=self.actualizar_dias
        )
        self.mes_menu.pack(pady=5)
        
        # Año
        ctk.CTkLabel(self.date_frame, text="Año:", font=("Arial", 14)).pack(pady=(10, 5))
        self.año_menu = ctk.CTkOptionMenu(
            self.date_frame, 
            values=self.años, 
            variable=self.año_var,
            font=("Arial", 14),
            width=200,
            command=self.actualizar_dias
        )
        self.año_menu.pack(pady=5)
        
        # Botones
        self.button_frame = ctk.CTkFrame(self.main_frame)
        self.button_frame.pack(pady=20, fill="x", padx=20)
        
        # Botón para obtener fecha
        self.btn_obtener = ctk.CTkButton(
            self.button_frame,
            text="📅 OBTENER FECHA",
            command=self.obtener_fecha,
            font=("Arial", 14, "bold"),
            height=40
        )
        self.btn_obtener.pack(pady=5, fill="x")
        
        # Botón para fecha actual
        self.btn_actual = ctk.CTkButton(
            self.button_frame,
            text="🔄 FECHA ACTUAL",
            command=self.fecha_actual,
            font=("Arial", 14),
            height=40,
            fg_color="gray",
            hover_color="darkgray"
        )
        self.btn_actual.pack(pady=5, fill="x")
        
        # Área de resultados
        self.result_frame = ctk.CTkFrame(self.main_frame)
        self.result_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Título resultados
        ctk.CTkLabel(
            self.result_frame, 
            text="📋 RESULTADOS:", 
            font=("Arial", 16, "bold")
        ).pack(pady=(10, 5))
        
        # Texto para mostrar resultados
        self.result_text = ctk.CTkTextbox(
            self.result_frame,
            height=150,
            font=("Arial", 12),
            wrap="word"
        )
        self.result_text.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Configurar texto como solo lectura
        self.result_text.configure(state="disabled")
        
        # Barra de estado
        self.status_bar = ctk.CTkLabel(
            self,
            text="Listo para seleccionar fecha",
            font=("Arial", 12),
            anchor="w"
        )
        self.status_bar.pack(side="bottom", fill="x", padx=20, pady=10)
        
        # Inicializar con fecha actual
        self.fecha_actual()
        
    def obtener_mes_numero(self, mes_nombre):
        """Convierte nombre de mes a número"""
        meses_dict = {
            "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
            "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
            "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
        }
        return meses_dict[mes_nombre]
    
    def obtener_fecha(self):
        """Obtiene y muestra la fecha seleccionada"""
        try:
            # Convertir mes de nombre a número
            mes_numero = self.obtener_mes_numero(self.mes_var.get())
            
            # Crear objeto datetime
            fecha = datetime(
                int(self.año_var.get()),
                mes_numero,
                int(self.dia_var.get())
            )
            
            # Formatear fecha en diferentes formatos
            fecha_formato1 = fecha.strftime("%d/%m/%Y")
            fecha_formato2 = fecha.strftime("%d-%m-%Y")
            fecha_formato3 = fecha.strftime("%Y/%m/%d")
            fecha_formato4 = fecha.strftime("%A, %d de %B de %Y")
            fecha_formato5 = fecha.strftime("%d/%m/%y")
            
            # Calcular día de la semana
            dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", 
                          "Viernes", "Sábado", "Domingo"]
            dia_semana = dias_semana[fecha.weekday()]
            
            # Mostrar resultados
            self.result_text.configure(state="normal")
            self.result_text.delete("1.0", "end")
            
            resultado = f"""
╔══════════════════════════════════════╗
║        FECHA SELECCIONADA            ║
╠══════════════════════════════════════╣
║                                      ║
║  📅 {fecha_formato4}  ║
║                                      ║
║  📌 Formato DD/MM/YYYY: {fecha_formato1}    ║
║  📌 Formato DD-MM-YYYY: {fecha_formato2}    ║
║  📌 Formato YYYY/MM/DD: {fecha_formato3}    ║
║  📌 Formato DD/MM/YY:   {fecha_formato5}    ║
║                                      ║
║  🌟 Día de la semana: {dia_semana}            ║
║                                      ║
╚══════════════════════════════════════╝

✅ Fecha válida seleccionada correctamente
            """
            
            self.result_text.insert("1.0", resultado)
            self.result_text.configure(state="disabled")
            
            # Actualizar barra de estado
            self.status_bar.configure(
                text=f"Fecha seleccionada: {fecha_formato1} - {dia_semana}",
                text_color="lightgreen"
            )
            
        except ValueError as e:
            # Mostrar error
            self.result_text.configure(state="normal")
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", f"❌ ERROR: Fecha inválida\n\nDetalle: {str(e)}")
            self.result_text.configure(state="disabled")
            
            self.status_bar.configure(
                text="Error: Fecha inválida seleccionada",
                text_color="red"
            )
    
    def fecha_actual(self):
        """Establece la fecha actual en los selectores"""
        ahora = datetime.now()
        
        self.dia_var.set(str(ahora.day))
        self.mes_var.set(self.meses[ahora.month - 1])
        self.año_var.set(str(ahora.year))
        
        # Actualizar días disponibles
        self.actualizar_dias()
        
        # Mostrar mensaje
        self.status_bar.configure(
            text=f"Fecha actual establecida: {ahora.day}/{ahora.month}/{ahora.year}",
            text_color="lightblue"
        )
    
    def actualizar_dias(self, *args):
        """Actualiza los días disponibles según mes y año"""
        try:
            mes_numero = self.obtener_mes_numero(self.mes_var.get())
            año = int(self.año_var.get())
            
            # Obtener número de días en el mes
            _, dias_en_mes = calendar.monthrange(año, mes_numero)
            
            # Actualizar lista de días
            nuevos_dias = [str(i) for i in range(1, dias_en_mes + 1)]
            self.dia_menu.configure(values=nuevos_dias)
            
            # Si el día actual es mayor que los días disponibles, ajustarlo
            if int(self.dia_var.get()) > dias_en_mes:
                self.dia_var.set(str(dias_en_mes))
                
        except:
            pass
    
    def validar_fecha(self, *args):
        """Valida que la fecha sea correcta"""
        try:
            mes_numero = self.obtener_mes_numero(self.mes_var.get())
            año = int(self.año_var.get())
            dia = int(self.dia_var.get())
            
            # Verificar si la fecha es válida
            datetime(año, mes_numero, dia)
            
            # Actualizar barra de estado
            fecha_str = f"{dia:02d}/{mes_numero:02d}/{año}"
            self.status_bar.configure(
                text=f"Fecha válida: {fecha_str}",
                text_color="white"
            )
            
        except ValueError:
            self.status_bar.configure(
                text="⚠️ Fecha inválida detectada",
                text_color="orange"
            )

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()