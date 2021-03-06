#Desde aquí se llama a la función que realiza el login y al mismo timepo une todas los archivos
from email.mime import base
from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter import *
import login
import funciones_admin
import funciones_estudiante
import base_de_datos
from cargar_en_archivos import cargar_archivos_admins, cargar_archivos_estudiantes, cargar_archivos_carreras, cargar_archivos_cursos
from funciones import lista_cursos, lista_carreras, lista_cursos_codigo
#shutil.copy('txt.txt', 'base_de_datos.py')
#msvcrt.getch()

ventana_login = tk.Tk()
ventana_login.title('Proyecto Taller')
ventana_login.minsize(800,600)

def cerrar_ventana_login():
    ventana_login.destroy()

def hide(x):
    for i in x:
        i.pack_forget()

def show(x):
    for i in x:
        i.pack()

def clear_text(x):
   for i in x:
        i.delete(0, END)

def mostrar_inicio():
    btn_login.pack()
    btn_reg.pack
    btn_salir.pack()


    

def mostrar_menu_e():
    btn_matricular_carrera.pack()
    btn_matricular_curso.pack()
    btn_registrar_actividad.pack()
    btn_determinar_estado.pack()




#Menu matricular carrera
sv_nombre_persona = tk .StringVar()
cb_carrera = ttk.Combobox(ventana_login, textvariable=sv_nombre_persona,width = 35)

def carreras():
    lista_carreras = []
    carreras = cargar_archivos_carreras()
    puntero = carreras
    while puntero.sig != None:
        lista_carreras.append(puntero.carrera)
        puntero = puntero.sig
    lista_carreras.append(puntero.carrera)
    return lista_carreras

cb_carrera['values'] =  carreras()
cb_carrera['state'] = 'readonly'
cb_carrera.pack_forget()

listbox_carreras = tk.Listbox(ventana_login)

def crear_listbox_carreras():
    lista = []
    carreras = cargar_archivos_carreras()
    puntero = carreras
    carreras_en_curso = u.carreras
    for i in carreras_en_curso:
        while puntero.sig != None:
            if i == puntero.codigo:
                lista.append(puntero.carrera)
            puntero = puntero.sig
        if puntero.sig == None:
            if i == puntero.codigo:
                lista.append(puntero.carrera)

    langs_var = tk.StringVar(value=lista)
    listbox_carreras.configure(listvariable=langs_var,height=6,selectmode='extended', width=35)
    listbox_carreras.pack()
    return listbox_carreras

btn_ingresar_carrera = tk.Button(ventana_login,text='Matricular')
btn_ingresar_carrera.configure(command= lambda: (funciones_estudiante.matricular_carrera(cb_carrera.get(), u, cargar_archivos_carreras),cb_carrera.set(''),crear_listbox_carreras()))
btn_ingresar_carrera.pack_forget()

#Menu matricular curso

def cursos():
    lista_cursos = []
    cursos = cargar_archivos_cursos()
    puntero = cursos
    while puntero.sig != None:
        lista_cursos.append(puntero.curso)
        puntero = puntero.sig
    lista_cursos.append(puntero.curso)
    return lista_cursos



sv_nombre_persona = tk .StringVar()
cb_curso = ttk.Combobox(ventana_login, textvariable=sv_nombre_persona, width=45)
cb_curso['values'] =  cursos()
cb_curso['state'] = 'readonly'
cb_curso.pack_forget()



listbox_curso = tk.Listbox(ventana_login)

def crear_listbox_cursos(si):
    if si == 'si':
        lista = []
        cursos = cargar_archivos_cursos()
        
        cursos_en_curso = u.cursos
        for i in cursos_en_curso:
            puntero = cursos
            while puntero.sig != None:
                if i == puntero.codigo:
                    lista.append(puntero.curso)
                puntero = puntero.sig
            if puntero.sig == None:
                if i == puntero.codigo:
                    lista.append(puntero.curso)


        contador = 1
        for i in lista:
            listbox_curso.insert(contador,i)
            print(i)
            contador =+ 1


        listbox_curso.configure(height=6,selectmode='extended', width=35)
        listbox_curso.pack()
        return listbox_curso
    elif si == 'no':
        listbox_curso.pack_forget()


btn_ingresar_curso = tk.Button(ventana_login,text='Matricular')
btn_ingresar_curso.configure(command= lambda: (listbox_curso.delete(0,END),funciones_estudiante.matricular_curso(cb_curso.get(), u, cargar_archivos_cursos,cargar_archivos_carreras),cb_carrera.set(''),crear_listbox_cursos('no'),crear_listbox_cursos('si')))
btn_ingresar_curso.pack_forget()


#Menu registrar actividad

sv_actividad = tk.StringVar()      
lb_actividad = tk.Label(ventana_login,text='Ingrese el nombre de la actividad: ')
e_actividad = ttk.Entry(ventana_login,textvariable = sv_actividad, width = 40)
lb_actividad.pack_forget
e_actividad.pack_forget()

sv_dia = tk.StringVar()      
lb_dia = tk.Label(ventana_login,text='Ingrese el dia de la actividad: ')
sv_cbdia = tk .StringVar()
cb_dia = ttk.Combobox(ventana_login,  textvariable=sv_cbdia)
cb_dia['values'] =  'lunes','martes','miercoles','jueves','viernes','sabado','domingo'
cb_dia['state'] = 'readonly'
cb_dia.pack_forget()

sv_hora_i = tk.StringVar()      
lb_hora_i = tk.Label(ventana_login,text='Ingrese la hora de inicio de la actividad: ')
sv_cbhora_i = tk .StringVar()
cb_hora_i = ttk.Combobox(ventana_login,  textvariable=sv_cbhora_i)
cb_hora_i['values'] =  [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
cb_hora_i['state'] = 'readonly'
cb_hora_i.pack_forget()

sv_hora_f = tk.StringVar()      
lb_hora_f = tk.Label(ventana_login,text='Ingrese la hora final de la actividad: ')
sv_cbhora_f = tk .StringVar()
cb_hora_f = ttk.Combobox(ventana_login,  textvariable=sv_cbhora_f)
cb_hora_f['values'] =  [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
cb_hora_f['state'] = 'readonly'
cb_hora_f.pack_forget()

lb_if = tk.Label(ventana_login,text='Esta su actividad relacionada con un curso?: ')
lb_if.pack_forget()

lb_curso_r = tk.Label(ventana_login,text='Ingrese la carrera seleccionada: ')
lb_curso_r.pack_forget()

radioValue = tk.IntVar()

rdioOne = tk.Radiobutton(ventana_login, text='Si', variable=radioValue, value=1) 
rdioTwo = tk.Radiobutton(ventana_login, text='No', variable=radioValue, value=2) 


sv_cursos = tk .StringVar()
cb_cursos = ttk.Combobox(ventana_login,  textvariable=sv_cursos)

def cargar_cursos_estudiante(usuario):
    lista_cursos = []
    curso = cargar_archivos_cursos()
    if usuario.cursos == []:
        return ''
    for i in usuario.cursos:
        puntero = curso
        while puntero.sig != None:
            if i == puntero.codigo:
                lista_cursos.append(puntero.curso)
            puntero = puntero.sig
        if puntero.sig == None and i == puntero.codigo:
            lista_cursos.append(puntero.curso)
    return lista_cursos

def crear_cb(usuario):
    if usuario != 'si':
        lista = cargar_cursos_estudiante(u)
        cb_cursos['values'] =  lista
        cb_cursos['state'] = 'readonly'
        cb_cursos.pack()
    elif usuario == 'no':
        cb_cursos.pack_forget()


listbox_actividades = tk.Listbox(ventana_login)

def crear_listbox_actividades(si):
    if si == 'si':
        lista = []
        dias =   ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']

        for i in dias:
            lista.append([i, u.actividades[i]])


        for y in lista:
            listbox_actividades.insert(7,y)



        listbox_actividades.configure(height=15,selectmode='extended', width=120)
        listbox_actividades.pack()
        return listbox_actividades
    elif si == 'no':
        listbox_actividades.pack_forget()




btn_ingresar_actividad = tk.Button(ventana_login,text = 'Registrar actividad')
btn_ingresar_actividad.configure(command= lambda: (listbox_actividades.delete(0,END),crear_listbox_actividades('no'), funciones_estudiante.ingresar_actividad(u,cargar_archivos_estudiantes ,e_actividad.get(),cb_dia.get(),cb_hora_i.get(),cb_hora_f.get(),radioValue.get(),cb_cursos.get()),crear_listbox_actividades('si')))
btn_ingresar_actividad.pack_forget

def si():
    x = radioValue.get()
    if x == 1:
        crear_cb(u)
        btn_ingresar_actividad.pack()
        x = 0
    elif x == 2:
        crear_cb('no')
        cb_cursos.set('')
        btn_ingresar_actividad.pack()





rdioOne.configure(command=si)
rdioTwo.configure(command=si)
rdioOne.pack_forget
rdioTwo.pack_forget

#Menu determinar estado

#Boton para salir
btn_log_out = tk.Button(ventana_login,text = 'Salir del usuario')
btn_log_out.configure(command= lambda: [show([btn_login,btn_reg,btn_salir]), hide([btn_log_out,btn_matricular_carrera,btn_matricular_curso,btn_registrar_actividad,btn_determinar_estado, cb_carrera, btn_ingresar_carrera, cb_curso, btn_ingresar_curso,lb_actividad, e_actividad,rdioOne,rdioTwo, lb_dia,cb_dia,lb_hora_i,cb_hora_i,lb_hora_f,cb_hora_f,cb_cursos,btn_ingresar_actividad,listbox_carreras])])
btn_log_out.pack_forget  

btn_aprobar = tk.Button(ventana_login,text = 'Aprobar')
btn_aprobar.configure(command= lambda: (funciones_estudiante.aprobar(u,cb_cursos.get()),crear_cb('no'),crear_cb('si'),cb_cursos.set('')))
btn_aprobar.pack_forget  

btn_reprobar = tk.Button(ventana_login,text = 'Reprobar')
btn_reprobar.configure(command= lambda: (funciones_estudiante.aprobar(u,cb_cursos.get()),crear_cb('no'),crear_cb('si'),cb_cursos.set('')))
btn_reprobar.pack_forget

#Menu admin:
def generar_ventana_agregar_curso():
    sv_nombre_curso = StringVar()
    sv_creditos_curso = StringVar()
    sv_horario_curso = StringVar()
    sv_inicial_horario = StringVar()
    sv_final_horario = StringVar()
    
    lb_nombre_curso = tk.Label(ventana_login, text='Escriba el nombre del curso que desea agregar') 
    e_nombre_curso = ttk.Entry(ventana_login, textvariable=sv_nombre_curso, width=40) 
    
    lb_creditos_curso = tk.Label(ventana_login, text='Escriba la cantidad de créditos del curso') 
    e_creditos_curso = ttk.Entry(ventana_login, textvariable=sv_creditos_curso, width=20) 
    
    lb_horario_curso = tk.Label(ventana_login, text='Elija el horario lectivo del curso')     
    cb_horario_curso = ttk.Combobox(ventana_login,  textvariable=sv_cbdia)
    cb_horario_curso['values'] =  'lunes','martes','miercoles','jueves','viernes','sabado','domingo'
    cb_horario_curso['state'] = 'readonly'
    
    lb_hora_inicial = tk.Label(ventana_login, text='Hora inicial, de 7 a 24')
    e_hora_inicial = ttk.Entry(ventana_login, textvariable=sv_inicial_horario) 
    
    lb_hora_final = tk.Label(ventana_login, text='Hora final, de 7 a 24')
    e_hora_final = ttk.Entry(ventana_login, textvariable=sv_final_horario) 
    
    btn_guardar_curso = tk.Button(ventana_login, text='Agregar curso')
    btn_guardar_curso.configure(command=lambda:(funciones_admin.agregar_curso(e_nombre_curso.get(), e_creditos_curso.get(), cb_horario_curso.get(), e_hora_inicial.get(), e_hora_final.get()), generar_ventana_agregar_curso()))
    
    btn_volver_menu = tk.Button(ventana_login, text='Volver al menú')
    btn_volver_menu.configure(command=lambda: (hide([lb_nombre_curso, e_nombre_curso, lb_creditos_curso, e_creditos_curso, lb_horario_curso, cb_horario_curso, lb_hora_inicial, e_hora_inicial, lb_hora_final, e_hora_final, btn_guardar_curso, btn_volver_menu]), generar_menu_admin()))
    
    return(show([lb_nombre_curso, e_nombre_curso, lb_creditos_curso, e_creditos_curso, lb_horario_curso, cb_horario_curso, lb_hora_inicial, e_hora_inicial, lb_hora_final, e_hora_final, btn_guardar_curso, btn_volver_menu]))


def generar_ventana_modificar_curso():
    sv_nombre_curso = StringVar()
    sv_creditos_curso = StringVar()
    sv_horario_curso = StringVar()
    sv_inicial_horario = StringVar()
    sv_final_horario = StringVar()
    
    lb_nombres_curso = tk.Label(ventana_login, text='Elija el curso que sea modificar') 
    cb_nombres_curso = ttk.Combobox(ventana_login, textvariable=sv_nombre_curso)
    cb_nombres_curso['values'] =  lista_cursos()
    cb_nombres_curso['state'] = 'readonly'
    
    lb_nombre_curso = tk.Label(ventana_login, text='Escriba el nuevo nombre del curso') 
    e_nombre_curso = ttk.Entry(ventana_login, textvariable=sv_nombre_curso, width=40) 
    
    lb_creditos_curso = tk.Label(ventana_login, text='Escriba la nueva cantidad de créditos del curso') 
    e_creditos_curso = ttk.Entry(ventana_login, textvariable=sv_creditos_curso, width=20) 
    
    lb_horario_curso = tk.Label(ventana_login, text='Elija el nuevo horario lectivo del curso')     
    cb_horario_curso = ttk.Combobox(ventana_login,  textvariable=sv_horario_curso)
    cb_horario_curso['values'] =  'lunes','martes','miercoles','jueves','viernes','sabado','domingo'
    cb_horario_curso['state'] = 'readonly'
    
    lb_hora_inicial = tk.Label(ventana_login, text='Hora inicial, de 7 a 24')
    e_hora_inicial = ttk.Entry(ventana_login, textvariable=sv_inicial_horario) 
    
    lb_hora_final = tk.Label(ventana_login, text='Hora final, de 7 a 24')
    e_hora_final = ttk.Entry(ventana_login, textvariable=sv_final_horario) 
    
    btn_guardar_curso = tk.Button(ventana_login, text='Modificar curso')
    btn_guardar_curso.configure(command=lambda:(funciones_admin.modificar_curso(cb_nombres_curso.get(), e_nombre_curso.get(), e_creditos_curso.get(), cb_horario_curso.get(), e_hora_inicial.get(), e_hora_final.get()), hide([lb_nombre_curso, e_nombre_curso, lb_creditos_curso, e_creditos_curso, lb_horario_curso, cb_horario_curso, lb_hora_inicial, e_hora_inicial, lb_hora_final, e_hora_final, btn_guardar_curso, btn_volver_menu, cb_nombres_curso, lb_nombres_curso]), generar_ventana_modificar_curso()))
    
    btn_volver_menu = tk.Button(ventana_login, text='Volver al menú')
    btn_volver_menu.configure(command=lambda: (hide([lb_nombre_curso, e_nombre_curso, lb_creditos_curso, e_creditos_curso, lb_horario_curso, cb_horario_curso, lb_hora_inicial, e_hora_inicial, lb_hora_final, e_hora_final, btn_guardar_curso, btn_volver_menu, cb_nombres_curso, lb_nombres_curso]), generar_menu_admin()))
    
    return(show([lb_nombres_curso, cb_nombres_curso, lb_nombre_curso, e_nombre_curso, lb_creditos_curso, e_creditos_curso, lb_horario_curso, cb_horario_curso, lb_hora_inicial, e_hora_inicial, lb_hora_final, e_hora_final, btn_guardar_curso, btn_volver_menu]))

def generar_ventana_agregar_carrera():
    sv_nombre_carrera = StringVar()
    sv_semestres = StringVar()
    sv_cusos = StringVar()
    langs_var = tk.StringVar(value=lista_cursos_codigo())
        
    lb_nombre_carrera = tk.Label(ventana_login, text='Escriba el nombre de la carrera que desea agregar') 
    e_nombre_carrera = ttk.Entry(ventana_login, textvariable=sv_nombre_carrera, width=40) 
    
    lb_semestres = tk.Label(ventana_login, text='Escriba la cantidad de semestres de la carrera') 
    e_semestres = ttk.Entry(ventana_login, textvariable=sv_semestres, width=20) 
    
    lis_cusos = tk.Listbox(ventana_login)
    lis_cusos.configure(listvariable=langs_var,height=6,selectmode='extended', width=35)
    
    lb_cursos = tk.Label(ventana_login, text='Escriba los codigos de los cursos que desea agregar separados por comas y un espacio') 
    e_cursos = ttk.Entry(ventana_login, textvariable=sv_cusos, width=20) 
    
    btn_guardar_carrera = tk.Button(ventana_login, text='Agregar carrera')
    btn_guardar_carrera.configure(command=lambda:(hide([lb_nombre_carrera, e_nombre_carrera, lb_semestres, e_semestres, lis_cusos, lb_cursos, e_cursos, btn_guardar_carrera, btn_volver_menu]), funciones_admin.agregar_carrera(e_nombre_carrera.get(), e_semestres.get(), e_cursos.get()), generar_ventana_agregar_carrera()))
    
    btn_volver_menu = tk.Button(ventana_login, text='Volver al menú')
    btn_volver_menu.configure(command=lambda: (hide([lb_nombre_carrera, e_nombre_carrera, lb_semestres, e_semestres, lis_cusos, lb_cursos, e_cursos, btn_guardar_carrera, btn_volver_menu]), generar_menu_admin()))
    
    return(show([lb_nombre_carrera, e_nombre_carrera, lb_semestres, e_semestres, lis_cusos, lb_cursos, e_cursos, btn_guardar_carrera, btn_volver_menu]))

def generar_ventana_modificar_carrera():
    sv_nombre_carrera = StringVar()
    sv_semestres = StringVar()
    sv_cusos = StringVar()
    langs_var = tk.StringVar(value=lista_cursos_codigo())
    
    lb_nombres_curso = tk.Label(ventana_login, text='Elija la carrera que sea modificar') 
    cb_nombres_curso = ttk.Combobox(ventana_login, textvariable=sv_nombre_carrera)
    cb_nombres_curso['values'] =  lista_carreras()
    cb_nombres_curso['state'] = 'readonly'
    
    lb_nombre_carrera = tk.Label(ventana_login, text='Escriba el nuevo nombre de la carrera') 
    e_nombre_carrera = ttk.Entry(ventana_login, textvariable=sv_nombre_carrera, width=40) 
    
    lb_semestres = tk.Label(ventana_login, text='Escriba la nueva cantidad de semestres de la carrera') 
    e_semestres = ttk.Entry(ventana_login, textvariable=sv_semestres, width=20) 
    
    lis_cusos = tk.Listbox(ventana_login)
    lis_cusos.configure(listvariable=langs_var,height=6,selectmode='extended', width=35)
    
    lb_cursos = tk.Label(ventana_login, text='Escriba los codigos de los cursos que desea agregar separados por comas') 
    e_cursos = ttk.Entry(ventana_login, textvariable=sv_cusos, width=20) 
    
    btn_guardar_carrera = tk.Button(ventana_login, text='Modificar carrera')
    btn_guardar_carrera.configure(command=lambda:(hide([lb_nombres_curso, cb_nombres_curso, lb_nombre_carrera, e_nombre_carrera, lb_semestres, e_semestres, lis_cusos, lb_cursos, e_cursos, btn_guardar_carrera, btn_volver_menu]), funciones_admin.modificar_carrera(cb_nombres_curso.get(), e_nombre_carrera.get(), e_semestres.get(), e_cursos.get()), generar_ventana_agregar_carrera()))
    
    btn_volver_menu = tk.Button(ventana_login, text='Volver al menú')
    btn_volver_menu.configure(command=lambda: (hide([lb_nombres_curso, cb_nombres_curso, lb_nombre_carrera, e_nombre_carrera, lb_semestres, e_semestres, lis_cusos, lb_cursos, e_cursos, btn_guardar_carrera, btn_volver_menu]), generar_menu_admin()))
    
    return(show([lb_nombres_curso, cb_nombres_curso, lb_nombre_carrera, e_nombre_carrera, lb_semestres, e_semestres, lis_cusos, lb_cursos, e_cursos, btn_guardar_carrera, btn_volver_menu]))
    
def generar_menu_admin():
    global btn_log_out
    
    btn_agregar_curso = tk.Button(ventana_login,text = 'Agregar curso')
    btn_agregar_curso.configure(command= lambda: (hide([btn_agregar_curso, btn_modificar_curso, btn_agregar_carrera, btn_modificar_carrera, btn_log_out]), generar_ventana_agregar_curso()))
    
    btn_modificar_curso = tk.Button(ventana_login,text = 'Modificar curso')
    btn_modificar_curso.configure(command= lambda: (hide([btn_agregar_curso, btn_modificar_curso, btn_agregar_carrera, btn_modificar_carrera, btn_log_out]), generar_ventana_modificar_curso()))

    btn_agregar_carrera = tk.Button(ventana_login,text = 'Agregar carrera')
    btn_agregar_carrera.configure(command= lambda: (hide([btn_agregar_curso, btn_modificar_curso, btn_agregar_carrera, btn_modificar_carrera, btn_log_out]), generar_ventana_agregar_carrera()))

    btn_modificar_carrera = tk.Button(ventana_login,text = 'Modificar carrera')
    btn_modificar_carrera.configure(command= lambda:(hide([btn_agregar_curso, btn_modificar_curso, btn_agregar_carrera, btn_modificar_carrera, btn_log_out]), generar_ventana_modificar_carrera()))
    
    return(show([btn_agregar_curso, btn_modificar_curso, btn_agregar_carrera, btn_modificar_carrera, btn_log_out]))



#Menu estudiante
btn_matricular_carrera = tk.Button(ventana_login,text = 'Matricular carrera')
btn_matricular_carrera.configure(command= lambda:(show([cb_carrera,btn_ingresar_carrera]),btn_atras.pack(side=BOTTOM), hide([btn_matricular_carrera, btn_matricular_curso,btn_registrar_actividad,btn_determinar_estado]),crear_listbox_carreras()))
btn_matricular_carrera.pack_forget

btn_matricular_curso = tk.Button(ventana_login,text = 'Matricular curso')
btn_matricular_curso.configure(command= lambda:(listbox_curso.delete(0,END),show([cb_curso,btn_ingresar_curso]),btn_atras.pack(side=BOTTOM),crear_listbox_cursos('si'),hide([btn_matricular_carrera, btn_matricular_curso,btn_registrar_actividad,btn_determinar_estado])))
btn_matricular_curso.pack_forget

btn_registrar_actividad = tk.Button(ventana_login,text = 'Registrar actividad')
btn_registrar_actividad.configure(command= lambda: (listbox_actividades.delete(0,END),hide([btn_matricular_carrera, btn_matricular_curso,btn_registrar_actividad,btn_determinar_estado]),show([lb_actividad,e_actividad, lb_dia,cb_dia,lb_hora_i,cb_hora_i,lb_hora_f,cb_hora_f,lb_if,rdioOne,rdioTwo]),crear_listbox_actividades('si'),btn_atras.pack(side=BOTTOM)))
btn_registrar_actividad.pack_forget

btn_determinar_estado = tk.Button(ventana_login,text = 'Determinar estado del curso')
btn_determinar_estado.configure(command= lambda: (hide([btn_matricular_carrera, btn_matricular_curso,btn_registrar_actividad,btn_determinar_estado]),crear_cb(u),show([btn_aprobar,btn_reprobar]),btn_atras.pack(side=BOTTOM)))
btn_determinar_estado.pack_forget

 

#Login

btn_atras = tk.Button(ventana_login,text = 'Regresar al menu')
btn_atras.configure(command= lambda: (show([btn_matricular_carrera,btn_matricular_curso,btn_determinar_estado,btn_log_out]), hide([cb_carrera,btn_ingresar_carrera,cb_curso,btn_ingresar_curso,listbox_carreras])))

def ingresar(bl):
    if type(bl[0]) == int:
        if bl[0] == 1:
            generar_menu_admin()
            btn_log_out.pack(side=BOTTOM)
        elif bl[0] == 2:
            global u
            u = bl[1]
            mostrar_menu_e()
            btn_log_out.pack(side=BOTTOM)
    else:
        return(generar_ventana_login())

def generar_ventana_login():
    sv_usuario = tk.StringVar()
    sv_contrasena = tk.StringVar()
        
    lb_usuario = tk.Label(ventana_login,text='Ingrese su nombre de usuario: ')
    e_usuario = ttk.Entry(ventana_login, textvariable = sv_usuario, width = 40)

    lb_contra = tk.Label(ventana_login,text='Ingrese su contraseña: ')
    e_contra = ttk.Entry(ventana_login,textvariable = sv_contrasena, width = 40)
    
    btn_ingresar = tk.Button(ventana_login,text = 'Ingresar')
    btn_ingresar.configure(command= lambda:
        [ingresar(login.login(sv_usuario.get(),sv_contrasena.get())),
         hide([lb_usuario, e_usuario, lb_contra, e_contra, btn_ingresar])])
    
    return(
        show([lb_usuario, e_usuario, lb_contra, e_contra, btn_ingresar])
    )
    
def generar_ventana_registrar():
    sv_new_name = StringVar()
    sv_new_num = StringVar()
    sv_new_user = StringVar()
    sv_new_pass = StringVar()
    
    lb_new_name = tk.Label(ventana_login, text="Ingrese su nombre")
    e_new_name = ttk.Entry(ventana_login, textvariable = sv_new_name, width = 40)
    
    lb_new_num = tk.Label(ventana_login, text="Ingrese su número de teléfono")
    e_new_num = ttk.Entry(ventana_login, textvariable = sv_new_num, width = 40)
    
    lb_new_user = tk.Label(ventana_login, text="Ingrese su usuario")
    e_new_user = ttk.Entry(ventana_login,textvariable = sv_new_user, width = 40)
    
    lb_new_pass = tk.Label(ventana_login, text="Ingrese su contraseña")
    e_new_pass = ttk.Entry(ventana_login, textvariable = sv_new_pass, width = 40)
    
    btn_registrar_admin = tk.Button(ventana_login, text = "Registrarse como Administrador")
    btn_registrar_admin.configure(command=lambda:
        [login.registrar(0, sv_new_name.get(), sv_new_num.get(), sv_new_user.get(), sv_new_pass.get())])
    btn_registrar_estud = tk.Button(ventana_login, text = "Registrarse como Estudiante")
    btn_registrar_estud.configure(command=lambda:
        [login.registrar(1, sv_new_name.get(), sv_new_num.get(), sv_new_user.get(), sv_new_pass.get())])
    
    return(show([lb_new_name, e_new_name, lb_new_num, e_new_num ,lb_new_user, e_new_user, lb_new_pass, e_new_pass, btn_registrar_admin, btn_registrar_estud]))

btn_login = tk.Button(ventana_login,text = 'Iniciar sesion')
btn_login.place(x=60,y=100)

btn_reg = tk.Button(ventana_login,text = 'Registrarse')
btn_reg.place(x=10,y=40)

btn_salir = tk.Button(ventana_login,text = 'Salir')
btn_salir.place(x=80,y=100)

#CONFIGURACIÓN DE LOS BOTONES DE LA PANTALLA DE INICIO
btn_login.configure(command=lambda:
    [hide([btn_salir,btn_login,btn_reg]), generar_ventana_login()])

btn_reg.configure(command=lambda:
    [hide([btn_salir,btn_login,btn_reg]), generar_ventana_registrar()])

btn_salir.configure(command = cerrar_ventana_login)

btn_login.pack()
btn_reg.pack()
btn_salir.pack()


tk.mainloop()