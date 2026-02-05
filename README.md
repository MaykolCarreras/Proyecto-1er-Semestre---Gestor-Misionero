# Gestor Misionero
Esta app esta diseñada para provecho de organizaciones misioneras. (i.e. Heartcry)
La siguiente app permite:
- Gestión de eventos
    - Ver/Añadir/Eliminar eventos en base a los recrusos disponibles

Por país tipo 
1
2
3

1 Entrega de recursos
2 Donación
3 Talleres
4 Conferencias

print("1. México")
print("2. Brasil")
print("3. Estados Unidos")

Gestionar personas
gestionar recursos
Taller necesita tratado


Notas durante desarrollo:
- Optimizar las bases de datos
- Optimizar los metodos de chequear exceptions
- Validar el salto de año, por ahora no voy a permitir eventos de un año para otro
- Modular todo llamando todo desde la función principal
- Ya casi todo esta hecho
- Falta diseñar la validación de los otros eventos, chequear() se usa en todos los casos para el "chequeo" de las timestamps
- Arreglar listar recursos y humanos
- Poner un validador asd para que se ponga la opcion ... etc
- arreglar los print solos con saltos de línea
- Las variables de aclaración han de estar en un json o algo así

añadir el evento al json ################
- Probar que datetime funciona en la validación de las fechas

El objetivo ahora es tener algo estable que presentar en el peor de los casos