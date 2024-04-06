from base_de_datos_tareas import tareas_lista
from ingreso_de_tareas import ingreso_id, titulo, descripcion, estado, fecha
from lista_de_tareas import filtrar_lista_tareas
from filtrar_tareas import filtrar_tareas, filtrar_tareas_titulo, filtrar_tareas_fecha, actualizar_tareas_id, actualizar_tareas_titulo, actualizar_tareas_descripcion, filtrar_tareas_descripcion, filtrar_tareas_estado, filtrar_tareas_titulo_nuevo, actualizar_tareas_estado

is_boolean_menu = True
while is_boolean_menu:

 print("Menu:")
 print("1. Lista de tareas")
 print("2. Filtrar tareas")
 print("3. Añadir tarea")
 print("4. Actualizar tarea")
 print("5. Eliminar tarea")
 print("6. Salir")

 opcion = input("Ingresa el numero de tu opcion a elegir: ")
 is_opcion = opcion.isdigit()

 while True:
     if is_opcion == True:
        is_number = int(opcion)
        if is_number == 1:
         print("Submenu")
         print("1. Tareas completadas")
         print("2. Tareas pendientes")
         print("3. Atras")
         opcion_submenu = input("Ingresa el numero de tu opcion: ")
         
         while not opcion_submenu.isdigit() or int(opcion_submenu) > 3:
             opcion_submenu = input("Ingresa una opcion valida solo numeros enteros sin espacios: ")
        
         opcion_submenu = int(opcion_submenu)
         
         if opcion_submenu == 1:
             print("Tareas completadas")
             tareas_completadas = filtrar_lista_tareas(opcion_submenu)
             for tareas in tareas_completadas:
                print(170 * '-')
                print('ID:',tareas['id'],'|','Titulo:',tareas['titulo'],'|','Descripcion: ',tareas['descripcion'],'|','Estado: ', tareas['estado'],'|','Fecha: ', tareas['fecha'])
                print(170 * '-') 
                
         elif opcion_submenu == 2:
             print("Tareas pendientes")
             tareas_pendientes = filtrar_lista_tareas(opcion_submenu)
             for tareas in tareas_pendientes:
                print(170 * '-')
                print('ID:',tareas['id'],'|','Titulo:',tareas['titulo'],'|','Descripcion: ',tareas['descripcion'],'|','Estado: ', tareas['estado'],'|','Fecha: ', tareas['fecha'])
                print(170 * '-') 
                
         elif opcion_submenu == 3:
             print("Haz tus tareas para que esten todas completadas compañero, hasta pronto!")
             
         else: print("Opcion invalida, solo aceptamos numeros enteros")
         
         break
     
        elif is_number > 6:
            print("Numero de opcion invalido, fuera de rango")
            break

        elif is_number == 2:
         print("Opcion 2 - Filtrar tareas")
         print("Submenu")
         print("1. Filtrar por codigo ID")
         print("2. Filtrar por titulo")
         print("3. Filtrar por fecha")
         print("4. Atras")
         opcion_submenu = input("Ingresa el numero de tu opcion: ")
         
         while not opcion_submenu.isdigit() or int(opcion_submenu) > 4:
             opcion_submenu = input("Ingresa una opcion valida solo numeros enteros sin espacios: ")
        
         opcion_submenu = int(opcion_submenu)
         
         if opcion_submenu == 1:
             print("Tareas por ID")
             numero_id = input("Ingresa tu numero de ID: ")
             while not numero_id.isdigit():
                 numero_id = input("Numero de ID invalido, ingresa solo numeros: ")
             numero_id = int(numero_id)
             tareas_id = filtrar_tareas(numero_id)
             for tareas in tareas_id:
                print(170 * '-')
                print('ID:',tareas['id'],'|','Titulo:',tareas['titulo'],'|','Descripcion: ',tareas['descripcion'],'|','Estado: ', tareas['estado'],'|','Fecha: ', tareas['fecha'])
                print(170 * '-') 
             break
     
         elif opcion_submenu == 2:
             print("Tareas por titulo")
             entrada_titulo = input("Ingresa tu titulo tomando en cuenta los espacios si tiene: ")
             while entrada_titulo == '':
                 entrada_titulo = input("Titulo invalido no se permiten numeros, ni string vacios: ")
             tareas_titulo = filtrar_tareas_titulo_nuevo(entrada_titulo)
             
             if tareas_titulo != []:
              for tareas in tareas_titulo:
                 print(170 * '-')
                 print('ID:',tareas['id'],'|','Titulo:',tareas['titulo'],'|','Descripcion: ',tareas['descripcion'],'|','Estado: ', tareas['estado'],'|','Fecha: ', tareas['fecha'])
                 print(170 * '-') 
                 
         
             else:print("El titulo ingresado no pertenece a ninguna tarea")
             break
            #  break
            
         elif opcion_submenu == 3:
             filtrado_fecha = fecha()
             tareas_filtradas_fecha = filtrar_tareas_fecha(filtrado_fecha)
             for tareas in tareas_filtradas_fecha:
                print(170 * '-')
                print('ID:',tareas['id'],'|','Titulo:',tareas['titulo'],'|','Descripcion: ',tareas['descripcion'],'|','Estado: ', tareas['estado'],'|','Fecha: ', tareas['fecha'])
                print(170 * '-') 
             break  
         elif opcion_submenu == 4:
             break     

        elif is_number == 3:
          diccionario = {}
          id_tarea = 0
          titulo_tarea = ''
          descripcion_tarea = ''
          estado_tarea = ''
          fecha_tarea = ''
          
          print("**************** Ingresa los siguientes datos para añadir tu tarea ****************")
            
          id_ingresado = ingreso_id()
          id_tarea = id_ingresado
             
          titulo_ingresado = titulo()
          titulo_tarea = titulo_ingresado
          
          descripcion_ingresada = descripcion()
          descripcion_tarea = descripcion_ingresada
          
          estado_ingresado = estado()
          estado_tarea = estado_ingresado
          
          fecha_ingresado = fecha()
          fecha_tarea = fecha_ingresado
          
          diccionario['id'] = id_tarea
          diccionario['titulo'] = titulo_tarea
          diccionario['descripcion'] = descripcion_tarea
          diccionario['estado'] = estado_tarea
          diccionario['fecha'] = fecha_tarea
          
          tareas_lista.append(diccionario)
          print("Tarea registrada con exito!! ")
          break
     
        elif is_number == 4:
         print("Para actualizar tu tarea necesitamos el numero de ID")
         entrada_id = input("Ingresa el ID de tu tarea: ")
         
         while not entrada_id.isdigit():
            entrada_id = input("Ingresaste un dato invalido, ingresa tu ID correcto: ")
        
         entrada_id = int(entrada_id)
         filtrado_id_unico = filtrar_tareas(entrada_id)
         
         if filtrado_id_unico != []:
            print("Submenu")
            print("1. Actualizar codigo")
            print("2. Actualizar titulo")
            print("3. Actualizar descripcion")
            print("4. Actualizar estado")
            print("5. Actualizar fecha")
            print("6. Atras")
            opcion_submenu = input("Ingresa el numero de tu opcion: ")
         
            while not opcion_submenu.isdigit() or int(opcion_submenu) > 6:
             opcion_submenu = input("Ingresa una opcion valida solo numeros enteros sin espacios: ")
        
            opcion_submenu = int(opcion_submenu)
         
            if opcion_submenu == 1:
                print("Actualizar ID")

                id_nuevo = input("Ingresa el ID a actualizar: ")
                
                while not id_nuevo.isdigit():
                  id_nuevo = input("Numero de ID invalido, ingresa solo numeros: ")
                  
                id_nuevo = int(id_nuevo)
                filtrado_id = list(filter(lambda id: id['id'] == id_nuevo, tareas_lista))
                 
                if filtrado_id != []:
                     print("tu ID no se pudo actualizar porque es el mismo numero")
                     break
                elif filtrado_id == []:
                     for codigo in tareas_lista:
                         diccionario = filtrado_id_unico[0]
                         if codigo['id'] == diccionario['id']:
                            codigo['id'] = id_nuevo
                            print("Tu ID ha sido actualizado con exito!")
                            break
                        
            elif opcion_submenu == 2:
                titulo_tarea = actualizar_tareas_titulo()
                filtrado_titulo = filtrar_tareas_titulo(titulo_tarea)
                
                if filtrado_titulo == []:
                        for titulo in filtrado_id_unico:
                         diccionario = filtrado_id_unico[0]
                         if titulo['titulo'] == diccionario['titulo']:
                            titulo['titulo'] = titulo_tarea
                            print("Tu titulo ha sido actualizado con exito!")
                            break
                elif filtrado_titulo != []:
                    print("tu titulo es igual al que ya tienes")
                    break
                
            elif opcion_submenu == 3:
                descripcion_tarea = actualizar_tareas_descripcion()
                filtrado_descripcion = filtrar_tareas_descripcion(descripcion_tarea)
                
                if filtrado_descripcion == []:
                        for descripcion in filtrado_id_unico:
                         diccionario = filtrado_id_unico[0]
                         if descripcion['descripcion'] == diccionario['descripcion']:
                            descripcion['descripcion'] = descripcion_tarea
                            print("Tu descripcion ha sido actualizado con exito!")
                            break
                elif filtrado_descripcion != []:
                    print("tu descripcion es igual a la que ya tienes")
                    break
            elif opcion_submenu == 4:
                estado_tarea = estado()
                filtrado_estado = filtrar_tareas_estado(estado_tarea)
                
                if filtrado_id_unico != []:
                         diccionario = filtrado_id_unico[0]
                         if diccionario['estado'] != estado_tarea:
                            diccionario['estado'] = estado_tarea
                            print("Tu estado ha sido actualizado con exito!")
                            break
                         elif diccionario['estado'] == estado_tarea['estado']:
                             print("Tu estado es igual al que ya tenia!")
                             break
                             
                elif filtrado_id_unico == []:
                    print("tu estado es igual a la que ya tienes")
                    break  
                
            elif opcion_submenu == 5:
                fecha_tarea = fecha()
                filtrado_fecha = filtrar_tareas_fecha(fecha_tarea)
                
                if filtrado_id_unico != []:
                         diccionario = filtrado_id_unico[0]
                         if diccionario['fecha'] != fecha_tarea:
                            diccionario['fecha'] = fecha_tarea
                            print("Tu fecha ha sido actualizado con exito!")
                            break
                         elif diccionario['fecha'] == fecha_tarea['fecha']:
                             print("Tu fecha es igual al que ya tenia!")
                             break
                             
                elif filtrado_id_unico == []:
                    print("tu fecha es igual a la que ya tienes")
                    break  
                
            elif opcion_submenu == 6:
                break                              
                
         elif filtrado_id_unico == []:
            print("Tu ID no existe!!")     
                   
         elif opcion_submenu == 2:
             entrada_titulo = input("Ingresa tu titulo ")
             
     
         elif opcion_submenu == 2:
             print("Tareas por titulo")
             entrada_titulo = input("Ingresa tu titulo tomando en cuenta los espacios si tiene: ")
             while entrada_titulo == '':
                 entrada_titulo = input("Titulo invalido no se permiten numeros, ni string vacios: ")
             tareas_titulo = filtrar_tareas_titulo(entrada_titulo)
             for tareas in tareas_titulo:
                print(170 * '-')
                print('ID:',tareas['id'],'|','Titulo:',tareas['titulo'],'|','Descripcion: ',tareas['descripcion'],'|','Estado: ', tareas['estado'],'|','Fecha: ', tareas['fecha'])
                print(170 * '-') 
                break
             else:print("El titulo ingresado no pertenece a ninguna tarea")
             break
            #  break
            
         elif opcion_submenu == 3:
             filtrado_fecha = fecha()
             tareas_filtradas_fecha = filtrar_tareas_fecha(filtrado_fecha)
             for tareas in tareas_filtradas_fecha:
                print(170 * '-')
                print('ID:',tareas['id'],'|','Titulo:',tareas['titulo'],'|','Descripcion: ',tareas['descripcion'],'|','Estado: ', tareas['estado'],'|','Fecha: ', tareas['fecha'])
                print(170 * '-') 
             break  
         elif opcion_submenu == 4:
             break     
         break
     
        elif is_number == 5:
           entrada_eliminar = input("Ingresa el numero ID de tu tarea a eliminar: ")
           
           while not entrada_eliminar.isdigit():
             entrada_eliminar = input("Ingresa un numero de ID valido: ")
             
           entrada_eliminar = int(entrada_eliminar)
           tareas_lista_copia = [tarea for tarea in tareas_lista]
           i = 0
           for tarea in tareas_lista_copia:
               if tarea['id'] == entrada_eliminar:
                           del tareas_lista[i]
                           print("Tu tarea ha sido eliminada con exito!")
                           break
                 
               elif tarea != entrada_eliminar:
                     i += 1   
           else: print("Tu ID no esta en nuestro sistema") 
           break 
             
        elif is_number == 6:
         print("HASTA PRONTO BUEN ESTUDIANTE!")
         is_boolean_menu = False
         break
     
     elif is_opcion == False:
         print("Dato invalido no se permiten letras ni espacios vacios")
         break
         
    #  else: print("Dato invalido no se permiten datos vacios ni letras, solo numeros, print else")