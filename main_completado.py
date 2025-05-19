import re #se encarga de imprimir el re.match para agregar caracteres especiales
from datetime import datetime  # Importar al inicio
import json
from rich import print
from rich.table import Table
from rich.console import Console
console = Console()    


def generar_hoja_de_vida(usuario, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("========== HOJA DE VIDA ==========\n\n")

        # DATOS PERSONALES
        dp = usuario["datosPersonales"]
        archivo.write(">> DATOS PERSONALES\n")
        archivo.write(f"Nombre: {dp['nombre']}\n")
        archivo.write(f"Número de Identificación: {dp['identificadores'][0]}\n")
        archivo.write(f"Fecha de Nacimiento: {dp['identificadores'][1]}\n")
        archivo.write(f"Celular: {dp['contacto']}\n")
        archivo.write(f"Dirección: {dp['dirección']}\n")
        archivo.write(f"Correo Electrónico: {dp['correo']}\n\n")

        # FORMACIÓN ACADÉMICA
        archivo.write(">> FORMACIÓN ACADÉMICA\n")
        for fa in usuario["formacionAcademica"]:
            archivo.write(f"- Universidad: {fa['Universidad']}\n")
            archivo.write(f"  Título: {fa['Titulo']}\n")
            archivo.write(f"  Año de Graduación: {fa['añoGraduación']}\n")
        archivo.write("\n")

        # EXPERIENCIA PROFESIONAL
        archivo.write(">> EXPERIENCIA PROFESIONAL\n")
        if usuario["experienciaProfesional"]:
            for exp in usuario["experienciaProfesional"]:
                archivo.write(f"- Empresa: {exp['Empresa']}\n")
                archivo.write(f"  Cargo: {exp['Cargo']}\n")
                archivo.write(f"  Duración: {exp['Duración']}\n")
        else:
            archivo.write("Sin experiencia laboral registrada.\n")
        archivo.write("\n")

        # REFERENCIAS PERSONALES
        archivo.write(">> REFERENCIAS PERSONALES\n")
        for ref in usuario["referenciasPersonales"]:
            archivo.write(f"- Nombre: {ref['nombre']}\n")
            archivo.write(f"  Relación: {ref['relación']}\n")
            archivo.write(f"  Teléfono: {ref['telefono']}\n")
        archivo.write("\n")

        # HABILIDADES ADICIONALES
        archivo.write(">> HABILIDADES ADICIONALES\n")
        if usuario["habilidadesAdicionales"]:
            for hab in usuario["habilidadesAdicionales"]:
                archivo.write(f"- {hab}\n")
        else:
            archivo.write("Sin habilidades adicionales registradas.\n")
        archivo.write("\n")

        archivo.write("==================================\n")

#Generar JSON general
def generarJsonCompleto(datos):
    path = "datos.json"
    with open(path, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
        print("json creado exitosamente")

#Filtrar hojas de vida por años de experiencia, devuelve un dict
def filtrarHojasAños(datos,limite):
    filtro=dict()
    for user,value in datos.items():
        for item in value["experienciaProfesional"]:
            if int(item["Duración"]) >= limite:
                filtro[user]=value
            else:
                continue
    return filtro
#generar JSON de filtro de años
def generarJsonAños(datosfiltradosAños):
    pathAños = "filtroAños.json"
    with open(pathAños, "w", encoding="utf-8") as file:
        json.dump(datosfiltradosAños, file, indent=4, ensure_ascii=False)
        print("json creado exitosamente")

#Filtrar hojas de vida por formación específica, devuelve un dict
def filtrarFormación(datos,formación):
    filtro=dict()
    for user,value in datos.items():
        for item in value["formacionAcademica"]:
            if item["Titulo"] == formación:
                filtro[user]=value
            else:
                continue
    return filtro
#generar JSON de filtro de formaciónes
def generarJsonFormacion(datosfiltradosFormación):
    pathFormación = "formación.json"
    with open(pathFormación, "w", encoding="utf-8") as file:
        json.dump(datosfiltradosFormación, file, indent=4, ensure_ascii=False)
        print("json creado exitosamente")

#Filtrar hojas de vida por habilidad específica, devuelve un dict
def filtrarHabilidades(datos,habilidad):
    filtro=dict()
    for user,value in datos.items():
        for item in value["habilidadesAdicionales"]:
            if item == habilidad:
                filtro[user]=value
            else:
                continue
    return filtro
#generar JSON de filtro de habilidades
def generarJsonHabilidades(datosfiltradosHabilidades):
    pathHabilidades = "habilidades.json"
    with open(pathHabilidades, "w", encoding="utf-8") as file:
        json.dump(datosfiltradosHabilidades, file, indent=4, ensure_ascii=False)
        print("json creado exitosamente")
         # Actualizar usuario
def actualizar_usuario(usuario_id):
    if usuario_id not in usuarios:
        print("Error: ID de usuario no encontrado.")
        return
def mostrarUsuarios(valor_a_buscar, tipo_busqueda):
    
    tabla = Table(title="Datos de la persona")
    tabla.add_column("nombre", style = "white", no_wrap=True)
    tabla.add_column("Identificacion", style = "white", no_wrap=True)
    tabla.add_column("Fecha de nacimiento", style = "white", no_wrap=True)
    tabla.add_column("contacto", style = "white", no_wrap=True)
    tabla.add_column("direccion", style = "white", no_wrap=True)
    tabla.add_column("correo", style = "white", no_wrap=True)
    tabla.add_column("titulo", style = "white", no_wrap=True)
    tabla.add_column("Años de experiencia", style = "white", no_wrap=True)
    

    
    
    for j,i in usuarios.items():
        datos = i['datosPersonales']
        formacion = i['experienciaProfesional'][0]
        formacion_academica = i['formacionAcademica'][0]

        # Busqueda por nombre
        if tipo_busqueda == "nombre" and datos['nombre'] == valor_a_buscar:
            tabla.add_row(
                datos['nombre'],
                datos['identificadores'][0],
                datos['identificadores'][1],
                datos['contacto'],
                datos['direccion'],
                datos['correo'],
                i['formacionAcademica'][0]['Titulo']
            )

        # Busqueda por documento (posición 0 de la tupla)
        elif tipo_busqueda == "documento" and datos['identificadores'][0] == valor_a_buscar:
            tabla.add_row(
                datos['nombre'],
                datos['identificadores'][0],
                datos['identificadores'][1],
                datos['contacto'],
                datos['direccion'],
                datos['correo'],
                i['formacionAcademica'][0]['Titulo']
            )

        # Búsqueda por correo
        elif tipo_busqueda == "correo" and datos['correo'] == valor_a_buscar:
            tabla.add_row(
                datos['nombre'],
                datos['identificadores'][0],
                datos['identificadores'][1],
                datos['contacto'],
                datos['direccion'],
                datos['correo'],
                i['formacionAcademica'][0]['Titulo']
            )
        elif tipo_busqueda == "Duracion" and int(formacion[tipo_busqueda]) >= int(valor_a_buscar):
            tabla.add_row(
                datos['nombre'],
                datos['identificadores'][0],
                datos['identificadores'][1],
                datos['contacto'],
                datos['direccion'],
                datos['correo'],
                i['formacionAcademica'][0]['Titulo'],
                i['experienciaProfesional'][0]['Duracion']

            )
            
        elif tipo_busqueda == "Titulo" and formacion_academica[tipo_busqueda] == valor_a_buscar:
            tabla.add_row(
                datos['nombre'],
                datos['identificadores'][0],
                datos['identificadores'][1],
                datos['contacto'],
                datos['direccion'],
                datos['correo'],
                i['formacionAcademica'][0]['Titulo'],
                i['experienciaProfesional'][0]['Duracion']

            )    
    console.print(tabla)

usuarios = {
    "1" : {
            "datosPersonales" : {
                "nombre":"J", 
                "identificadores":("1000456789","12/88/2005"),
                "contacto": "31359450559",
                "dirección": "Cra12 #34 A 45",
                "correo": "miguelarias@gmail.com",},
            
            "formacionAcademica" : [{"Universidad": "ECCI","Titulo":"Profesional lenguas modernas", "añoGraduación": "2024"}],
            
            "experienciaProfesional" : [{"Empresa":"Teleperformance", "Cargo":"Asesor Bilingüe", "Duración": "10"}, {"Empresa":"Concentrix", "Cargo":"Asesor Bilingüe", "Duración": "4 meses"}],
            "referenciasPersonales": [{"nombre":"miguel angel arias marin II", "relación": "vecino", "telefono": "3205118016"}],
            "habilidadesAdicionales": ["HTML","CSS","Python","Inglés B2", "Diploma Pedagogía"]
    }
}
serial = len(usuarios)

def datosPersonalesDict(nombre,identificacion,fecha,contacto,direccion,correo):
    lista=[identificacion,fecha]
    tupla=tuple(lista)
    diccionario={"nombre":nombre,"identificadores":tupla,"contacto":contacto,"dirección":direccion,"correo":correo}
    return diccionario
    
def formaciónDict(universidad,titulo,año):
    diccionario={"Universidad":universidad,"Titulo":titulo, "añoGraduación":año}
    return diccionario
def referenciasDict(nombre,relación,telefono):
    diccionario={"nombre":nombre,"relación":relación, "telefono":telefono}
    return diccionario

def actualizar_usuario(usuario_id):
    if usuario_id not in usuarios:
        print("Error: ID de usuario no encontrado.")
        return

añadir=True
while añadir:
    serial += 1
    usuarios[str(serial)] = {}
    listaFormaciones=[]
    listaReferencias=[]
    experiencias = []
    habilidades = []

    #DatosPersonales
    datosPersonales= print("A continuacion se le pediran sus datos personales")
    while True:
        nombre=input("Ingresa tu nombre: ")
        if nombre.isalpha():
            break
        else:
            print("Ingresa un nombre valido.")
    while True:
        identificacion=input("Agrega tu numero de identidad: ")
        if identificacion.isdigit() and 8<= len(identificacion) <= 10 :
            break
        else:
            print("La identificacion no es válida: ")
    while True:    
        fecha_nacimiento=input("Ingresa tu fecha de nacimiento (DD/MM/AA): ")
        try:
            fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            hoy = datetime.now()
            if fecha >= hoy:
                print("La fecha no puede ser el dia actual")
            else:
                print("Fecha válida:", fecha.strftime("%d/%m/%Y"))
            break
        except ValueError:
            print("Error: Formato de fecha inválido. Usa DD/MM/YYYY (ej: 15/05/2000).")
    while True:
        celular_numero=input("Ingresa tu numero de celular: ")
        if celular_numero.isdigit() and len(celular_numero) == 10:
            break
        else:
            print("El numero de celular no es válido")
    while True:
        direccion=input("Ingresa la direccion de tu vivienda: ")
        if re.match(r'^[a-zA-Z0-9\sáéíóúñÁÉÍÓÚÑ#\-/.,()]+$', direccion):
            if len(direccion) >=5:
                print("Direccion valida ")
                break
            else:
                print("La direccion debe de contener al menos 5 caracteres (Debe ser real)")
        else:
            print("Error: La dirección solo puede contener letras, números, espacios, #, -, /, ., ,, () y acentos.")
    while True:
        correo_elect=input("Ingresa tu correo electronico:")
        if  re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo_elect):
            if len(correo_elect) <=100:
                    print("El correo ha sido agregado")
                    break
            else:
                print("El correo debe tener minimo 100 caracteres")
        else:
            print("El correo debe de tener los siguientes caracteres(ej. ejemplo@dominio.com)")
    datosPersonales = datosPersonalesDict(nombre,identificacion,fecha_nacimiento,celular_numero,direccion,correo_elect)   

    #formacion académica:
    print("A continuacion se le pediran su información académica")
    while True:
        while True: 
            universidad = input("Ingresa el nombre de la universidad: ")
            if universidad.replace(" ", "").isalpha(): 
                break
            else:
                print("Ingresa un nombre válido")
        while True: 
            titulo = input("Ingresa el nombre del título: ")
            if titulo.replace(" ", "").isalpha(): 
                break
            else:
                print("Ingresa un nombre válido")
        while True: 
            año = input("Ingresa el año de graduación: ")
            if año.isdigit(): 
                break
            else:
                print("Ingresa un año válido")
                                
        formacion = formaciónDict(universidad,titulo,año)
        listaFormaciones.append(formacion)
        while True: 
            reset = input("¿Quieres añadir más formación profesional? 1.Si/2.No: ")
            if reset.isdigit()==False:
                print("Ingresa una opción válida (1/2)")
            elif int(reset) != 1 and int(reset) != 2:
                print("Ingresa una opción válida (1/2)")
            else:
                break
        if int(reset) == 2:
            break               

    #Experiencias
    print("A continuacion se le pedirá su experiencia laboral")
    experiencia = input("¿Tienes experiencia laboral? 1.Si/2.No: ")
    while True:
        
        if experiencia == "1":
            while True:
                Empresa = input("Empresa donde trabajo: ")
                if  Empresa.replace(" ", "").isalpha():
                    break
                else:
                    print("Ingrese un nombre valido\n")
            while True:
                    cargo = input("¿Que cargo ejercias?: ")
                    if  cargo.replace(" ", "").isalpha():
                        break
                    else:
                        print("Ingrese un nombre valido\n")
            while True:
                    duracion = input("¿Tiempo de duracion (cantidad en años)?: ")
                    if  duracion.isdigit():
                        break
                    else:
                        print("Ingrese un nombre valido\n")
                        
            informacion = {"Empresa":Empresa, "Cargo":cargo, "Duración": duracion}
            
            experiencias.append(informacion)            
            salir = input("¿Quieres ingresar mas expreciencias laborales? (si/no): ")
            if salir == "2":
                break
        else:
            print("a bueno")
            break

    #referenciasPersonales
    print("A continuacion se le pedirán sus referencias personales")
    while True:
        while True: 
            nombreRef = input("Ingresa el nombre de tu referencia : ")
            if nombreRef.replace(" ", "").isalpha(): 
                break
            else:
                print("Ingresa un nombre válido")
        while True: 
            relacion = input("Ingresa tu relación con esta persona: ")
            if relacion.replace(" ", "").isalpha(): 
                break
            else:
                print("Ingresa un dato válido")
        while True: 
            telefonoRef = input("Ingresa el teléfono de tu referencia: ")
            if telefonoRef.isdigit() and len(telefonoRef) == 10: 
                break
            else:
                print("Ingresa un teléfono válido")
                                
        referencias = referenciasDict(nombreRef,relacion,telefonoRef)
        listaReferencias.append(referencias)
        while True: 
            reset = input("¿Quieres añadir más referencias 1.Si/2.No: ")
            if reset.isdigit()==False:
                print("Ingresa una opción válida (1/2)")
            elif int(reset) != 1 and int(reset) != 2:
                print("Ingresa una opción válida (1/2)")
            else:
                break
        if int(reset) == 2:
            break
            
    #Habilidades adicionales
    habilidadesAdicionales = input("¿Tienes habilidades adicionales? 1.Si/2.No: ")
    while True: 
        if habilidadesAdicionales == "1":
            while True:
                habilidad = input("Digite una habilidad: ")
                if  habilidad.replace(" ", "").isalpha():
                    break
                else:
                    print("Ingrese texto valido valido\n")
                                
            habilidades.append(habilidad)            
            salir = input("¿Quieres ingresar otra habilidad? 1.Si/2.No: ")
            if salir == "2":
                break
        else:
            break
            
    usuarios[str(serial)]["datosPersonales"] = datosPersonales
    usuarios[str(serial)]["formacionAcademica"] = listaFormaciones
    usuarios[str(serial)]["experienciaProfesional"] = experiencias
    usuarios[str(serial)]["referenciasPersonales"] = listaReferencias
    usuarios[str(serial)]["habilidadesAdicionales"] = habilidades
    
    generar_hoja_de_vida(usuarios[str(serial)],"miguel.txt")
    
    
    salir = input("¿Quieres añadir otro usuario? 1.Si/2.No: ")
    if salir == "2":
        añadir=False

   #Consultar hojas de vida 
print("Bienvenido a consultar hojas de vida\n")
opciones = input("(1).Buscar por informacion  \n(2).filtrar informacion \n(3).Correo electronico \n>>>")
match opciones:
    case "1":
        print("Opciones de busqueda: ")
        opciones = input("(1).Nombre  \n(2).documento \n(3).Correo electronico \n>>>")

        match opciones:
            case "1":
                console.print("[bold cyan]Búsqueda por nombre[/bold cyan]")
                nombre = input("Ingrese el nombre a buscar: \n>>> ")
                mostrarUsuarios(nombre, "nombre")
            case "2":
                console.print("[bold cyan]Búsqueda por documento[/bold cyan]")
                documento = input("Ingrese el documento a buscar: \n>>> ")
                mostrarUsuarios(documento, "documento")
            case "3":
                console.print("[bold cyan]Búsqueda por correo[/bold cyan]")
                email = input("Ingrese el correo a buscar: \n>>> ")
                mostrarUsuarios(email, "correo")
    case "2":
        print("Opciones de filtros: ")
        opciones = input("(1).Años de experiencia  \n(2).Titulo profesional \n(3).habilidades \n>>>")
        match opciones:
            case "1":
                print("filtrar por años de experiencia")
                años_experiencia = input("Digite el minimo de años de experiencia: ")
                mostrarUsuarios(años_experiencia,"Duracion")
            case "2":
                print("filtrar por titulo profesional")
                titulo_profesional = input("Digite el minimo de años de experiencia: ")
                mostrarUsuarios(titulo_profesional,"Titulo")

 # Actualizar usuario
def actualizar_usuario(usuario_id): 
    if usuario_id not in usuarios:
        print("Error: ID de usuario no encontrado.")
        return
    
    while True:
        print("\nOpciones de actualización para el usuario", usuario_id)
        print("1. Añadir nueva experiencia o formación")
        print("2. Editar datos personales o de contacto")
        print("3. Agregar habilidades y referencias")
        print("4. Volver al menú principal")

        try:
            seleccione_act = int(input("Selecciona una opción (1-4): "))
        except ValueError:
            print("Error: Ingresa un número válido.")
            continue

        if seleccione_act == 1:
            tipo = input("¿Deseas añadir experiencia (1) o formación (2)? Ingresa 1 o 2: ")
            if tipo == "1":
                while True:
                    empresa = input("Ingresa el nombre de la empresa: ")
                    if empresa.replace(" ", "").isalpha():
                        break
                    print("Ingrese un nombre valido\n")
                while True:
                    cargo = input("Ingresa el cargo: ")
                    if cargo.replace(" ", "").isalpha():
                        break
                    print("Ingrese un nombre valido\n")
                while True:
                    duracion = input("Ingresa la duración (cantidad en años): ")
                    if duracion.isdigit():
                        break
                    print("Ingrese un número valido\n")
                informacion = {"Empresa": empresa, "Cargo": cargo, "Duración": duracion}
                usuarios[usuario_id]["experienciaProfesional"].append(informacion)
                print("Experiencia añadida.")
            elif tipo == "2":
                while True:
                    universidad = input("Ingresa el nombre de la universidad: ")
                    if universidad.replace(" ", "").isalpha():
                        break
                    print("Ingresa un nombre válido")
                while True:
                    titulo = input("Ingresa el nombre del título: ")
                    if titulo.replace(" ", "").isalpha():
                        break
                    print("Ingresa un nombre válido")
                while True:
                    año = input("Ingresa el año de graduación: ")
                    if año.isdigit():
                        break
                    print("Ingresa un año válido")
                formacion = formaciónDict(universidad, titulo, año)
                usuarios[usuario_id]["formacionAcademica"].append(formacion)
                print("Formación añadida.")
            else:
                print("Opción inválida.")

        elif seleccione_act == 2:
            print("\nDatos actuales:", usuarios[usuario_id]["datosPersonales"])
            tipo = input("¿Deseas cambiar dirección (1) o número (2)? Ingresa 1 o 2: ")
            if tipo == "1":
                while True:
                    direccion = input("Ingresa la nueva dirección: ")
                    if re.match(r'^[a-zA-Z0-9\sáéíóúñÁÉÍÓÚÑ#\-/.,()]+$', direccion):
                        if len(direccion) >= 5:
                            print("Dirección valida ")
                            usuarios[usuario_id]["datosPersonales"]["dirección"] = direccion
                            print("Dirección actualizada.")
                            break
                        else:
                            print("La dirección debe contener al menos 5 caracteres")
                    else:
                        print("Error: La dirección solo puede contener letras, números, espacios, #, -, /, ., ,, () y acentos.")
            elif tipo == "2":
                while True:
                    celular_numero = input("Ingresa el nuevo número de celular: ")
                    if celular_numero.isdigit() and len(celular_numero) == 10:
                        usuarios[usuario_id]["datosPersonales"]["contacto"] = celular_numero
                        print("Número actualizado.")
                        break
                    else:
                        print("El número de celular no es válido")
            else:
                print("Opción inválida.")

        elif seleccione_act == 3:
            tipo = input("¿Deseas añadir habilidad (1) o referencia (2)? Ingresa 1 o 2: ")
            if tipo == "1":
                while True:
                    habilidad = input("Ingresa una habilidad: ")
                    if habilidad.replace(" ", "").isalpha():
                        if habilidad not in usuarios[usuario_id]["habilidadesAdicionales"]:
                            usuarios[usuario_id]["habilidadesAdicionales"].append(habilidad)
                            print("Habilidad añadida.")
                            break
                        else:
                            print("Error: La habilidad ya existe.")
                    else:
                        print("Ingrese texto valido\n")
            elif tipo == "2":
                while True:
                    nombreRef = input("Ingresa el nombre de la referencia: ")
                    if nombreRef.replace(" ", "").isalpha():
                        break
                    print("Ingresa un nombre válido")
                while True:
                    relacion = input("Ingresa la relación con esta persona: ")
                    if relacion.replace(" ", "").isalpha():
                        break
                    print("Ingresa un dato válido")
                while True:
                    telefonoRef = input("Ingresa el teléfono de la referencia: ")
                    if telefonoRef.isdigit() and len(telefonoRef) == 10:
                        break
                    print("Ingresa un teléfono válido")
                referencias = referenciasDict(nombreRef, relacion, telefonoRef)
                usuarios[usuario_id]["referenciasPersonales"].append(referencias)
                print("Referencia añadida.")
            else:
                print("Opción inválida.")

        elif seleccione_act == 4:
            break

        else:
            print("Opción inválida.")

        # Actualizar hoja de vida y JSON
        generar_hoja_de_vida(usuarios[usuario_id], f"hoja_vida_{usuario_id}.txt")
        generarJsonCompleto(usuarios)
    
