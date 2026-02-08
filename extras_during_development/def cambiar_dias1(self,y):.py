def cambiar_dias1(self,y):
        y = int(y)
        if (y%400==0 or (y%4==0 and y%100!=0)) and self.mes.get() == "Febrero":
            self.seleccion_dia.configure(values=self.dias29)


def cambiar_dias2(self,m):
        y=int(self.año.get())
        if m=="Febrero" and (y%400==0 or (y%4==0 and y%100!=0)):
            self.seleccion_dia.configure(values=self.dias29)
            return 
        
        if m=="Febrero":
            self.seleccion_dia.configure(values=self.dias28)

        if m=="Enero" or m=="Marzo" or m=="Mayo" or m=="Julio" or m=="Agosto" or m=="Octubre" or m =="Diciembre":
            self.seleccion_dia.configure(values=self.dias31)

        if m=="Febrero":
            self.seleccion_dia.configure(values=self.dias30)