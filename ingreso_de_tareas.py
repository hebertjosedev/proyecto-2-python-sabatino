from datetime import datetime
from base_de_datos_tareas import tareas_lista

diccionario_nuevo = {}

def ingreso_id():
    entrada = input("Ingresa un ID numerico: ")
    
    while not entrada.isdigit():
        print("El ID no puede ser un dato vacio ni letras")
        entrada = input("Ingresa nuevamente un ID valido: ")
        
    if entrada.isdigit() == True:
        entrada = int(entrada)
        resultado_filtrado = filtrado(entrada)
         
        if resultado_filtrado == True:
            print("Tu ID es invalido, porque coincide con uno ya creado!")
            return ingreso_id()
            
    return entrada

def filtrado(id_ingresado):
    filtrado = list(filter(lambda id: id['id'] == id_ingresado, tareas_lista))
    
    if filtrado == []:
        is_boolean = False
        return is_boolean
    
    elif filtrado != []:
        is_boolean = True
        return is_boolean
        
            
             
def titulo():
    titulo = ''
    titulo_entrada = input("Ingresa un titulo que no sea mayor a 20 caracteres: ")

    while titulo_entrada == '' or len(titulo_entrada) > 20:
        print("Ingresa un dato valido, no se aceptan datos vacios ni mas de 20 caracteres para el titulo")
        titulo_entrada = input("Ingresa nuevamente tu titulo: ")
        
    if titulo_entrada != '':
        titulo = titulo_entrada
        return titulo
    
def descripcion():
    descripcion = ''
    descripcion_entrada = input("Ingresa una descripcion sin importar el numero de caracteres: ")
    
    while descripcion_entrada == '':
        print("Ingresa un dato valido, tu descripcion no puede estar vacia")
        descripcion_entrada = input("Ingresa nuevamente tu descripcion correctamente: ")
        
    descripcion = descripcion_entrada
    return descripcion

def estado():
    estado_tarea = ''
    estado_entrada = input("Ingresa el estado de tu tarea COMPLETADA O PENDIENTE: ").lower()
    is_boolean = True
    
    if estado_entrada == 'completada' or estado_entrada == 'pendiente':
        estado_tarea = estado_entrada
        is_boolean = False
        return estado_tarea

    while is_boolean:
        print("Ingresa un estado valido; ya sea completado o pendiente")
        estado_entrada = input("Ingresa nuevamente tu estado correctamente: ")
        
        if estado_entrada == 'completada' or estado_entrada == 'pendiente':
         estado_tarea = estado_entrada
         is_boolean = False
         return estado_tarea

def fecha():
    fecha_tarea = ''
    
    while True:
        try:
            fecha_entrada = input("Ingrese la fecha de su tarea (DD-MM-YYYY): ")
            fecha_entrada = datetime.strptime(fecha_entrada, '%d-%m-%Y')
            fecha_formateada = fecha_entrada.strftime("%d-%m-%Y")
            fecha_tarea = fecha_formateada
            return fecha_tarea

        except ValueError:
            print("ERROR: Debe digitar una fecha valida con el formato DD-MM-YYYY.")
            