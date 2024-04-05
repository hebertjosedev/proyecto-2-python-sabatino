from base_de_datos_tareas import tareas_lista

def filtrar_lista_tareas(entrada):
    if entrada == 1:
        filtrar_tareas_completadas = list(filter(lambda tarea: tarea['estado'] == 'completada', tareas_lista))
        return filtrar_tareas_completadas
    
    elif entrada == 2:
        filtrar_tareas_pendientes = list(filter(lambda tarea: tarea['estado'] == 'pendiente', tareas_lista))
        return filtrar_tareas_pendientes