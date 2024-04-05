from base_de_datos_tareas import tareas_lista
from datetime import datetime

def filtrar_tareas(entrada):
    if entrada != 0:
        filtrar_tareas_id = list(filter(lambda tarea: tarea['id'] == entrada, tareas_lista))
        return filtrar_tareas_id
    
    # elif entrada != '':
    #      filtrar_tareas_titulo = list(filter(lambda tarea: tarea['titulo'] == entrada, tareas_lista))
    #      return filtrar_tareas_titulo
     
def filtrar_tareas_titulo(entrada):
        if entrada != '':
         filtrar_tareas_titulo = list(filter(lambda tarea: tarea['titulo'] == entrada, tareas_lista))
         return filtrar_tareas_titulo
     
def filtrar_tareas_fecha(entrada):
        if entrada != '':
         filtrar_tareas_titulo = list(filter(lambda tarea: tarea['fecha'] == entrada, tareas_lista))
         return filtrar_tareas_titulo