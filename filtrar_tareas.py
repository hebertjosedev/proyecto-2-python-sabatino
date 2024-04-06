from base_de_datos_tareas import tareas_lista
from datetime import datetime

def filtrar_tareas(entrada):
    if entrada != 0:
        filtrar_tareas_id = list(filter(lambda tarea: tarea['id'] == entrada, tareas_lista))
        return filtrar_tareas_id
     
def filtrar_tareas_titulo(entrada):
        if entrada != '':
         filtrar_tareas_titulo = list(filter(lambda tarea: tarea['titulo'] == entrada, tareas_lista))
         return filtrar_tareas_titulo
     
def filtrar_tareas_titulo_nuevo(entrada):
    resultado = [palabra for palabra in tareas_lista if palabra['titulo'][0:3] == entrada[0:3]]
    return resultado

filtrar_tareas_titulo_nuevo('aprender')
     
filtrar_tareas_titulo_nuevo('equipos')
     
def filtrar_tareas_descripcion(entrada):
        if entrada != '':
         filtrar_tareas_descripcion = list(filter(lambda tarea: tarea['descripcion'] == entrada, tareas_lista))
         return filtrar_tareas_descripcion
     
def filtrar_tareas_estado(entrada):
        if entrada != '':
         filtrar_tareas_estado = list(filter(lambda tarea: tarea['estado'] == entrada, tareas_lista))
         return filtrar_tareas_estado
     
def filtrar_tareas_fecha(entrada):
        if entrada != '':
         filtrar_tareas_titulo = list(filter(lambda tarea: tarea['fecha'] == entrada, tareas_lista))
         return filtrar_tareas_titulo
     
def actualizar_tareas_id(entrada):
    if entrada != 0:
        filtrar_tareas_id = dict(filter(lambda tarea: tarea['id'] == entrada, tareas_lista))
        return filtrar_tareas_id
    
def actualizar_tareas_titulo():
    entrada = input("Ingresa tu titulo a actualizar: ")
    
    while entrada == '':
        print("El titulo no puede ser un dato vacio")
        entrada = input("Ingresa nuevamente un titulo valido: ")
     
    return entrada

def actualizar_tareas_descripcion():
    entrada = input("Ingresa tu descripcion a actualizar: ")
    
    while entrada == '':
        print("El titulo no puede ser un dato vacio")
        entrada = input("Ingresa nuevamente un titulo valido: ")
     
    return entrada

def actualizar_tareas_estado():
    entrada = input("Ingresa tu estado a actualizar: ")
    
    while entrada == '':
        print("El estado no puede ser un dato vacio")
        entrada = input("primer while Ingresa nuevamente un titulo valido: ")
        
    if entrada == 'completado' or entrada == 'pendiente':
        return entrada
    
    while entrada != 'completado' or entrada != 'pendiente':
        print("El estado no puede ser diferente a completado y pendiente")
        entrada = input("segundo while Ingresa nuevamente tu estado valido: ")
     
    return entrada

def actualizar_tareas_fecha():
    entrada = input("Ingresa tu titulo a actualizar: ")
    
    while entrada == '':
        print("El titulo no puede ser un dato vacio")
        entrada = input("Ingresa nuevamente un titulo valido: ")
     
    return entrada

