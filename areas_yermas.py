from tkinter import *
from tkinter import font

'''
COMANDO MATANZAS: 13:25 HORAS, SALIÓ LA TÉCNICA AC-2A, CON SU DOTACIÓN EN DIRECCIÓN A LA CARRETERA A LAS CUEVAS EN EL CONSEJO POPULAR PLAYA PUEBLO NUEVO,
DONDE SE ORIGINÓ UN PRINCIPIO DE INCENDIO Q-101 EN ÁREAS YERMAS.  NO REPORTÁNDOSE PÉRDIDAS O LESIONADOS, DETERMINÁNDOSE LA CAUSA DEL SURGIMIENTO LA # 16
COMBUSTIÓN EN ÁREAS YERMAS, BASUREROS Y DESPERDICIOS SÓLIDOS. CONCLUIDO EL SERVICIO SE RETIRAN DE LA DIRECCIÓN ANTES MENCIONADA, SURTEN SUSTANCIAS
EXTINTORAS, ENTRANDO AL COMANDO A LAS XX:XX HORAS.
'''

root = Tk()
root.title("Areas Yermas")
root.iconbitmap("icon.ico")

#Cambio de fuente
fuente = font.Font(family="Tahoma", size = 12)
root.option_add("*Font", fuente)

'''
=====================================================================================================================================================
#Creando
=====================================================================================================================================================
'''

#Creando listas para los OptionMenu
lista_comandos = ["Matanzas","Supertanqueros","Aeropuerto","Santa Marta","Cárdenas","Colón","Jovellanos","Unión","Jagüey","Calimete","Avanzada"]
lista_clasificaciones = ["Q-101","Q-102","Q-103","Q-104","Q-105"]
lista_causas_full = [
    '#01 CONDUCTORES ELÉCTRICOS CON DEFICIENTE AISLAMIENTO',
    '#02 EQUIPOS Y APARATOS ELÉCTRICOS EN MAL ESTADO TÉCNICO',
    '#03 DISPOSITIVOS DE CONTROL DEFECTUOSO O INEXISTENTE',
    '#04 FALTA O INSUFICIENTE PROTECCIÓN DE LOS EQUIPOS Y APARATOS ELÉCTRICOS',
    '#05 SOBRECARGA ELÉCTRICA EN LAS LÍNEAS',
    '#06 SOBRECARGA MECÁNICA EN EQUIPOS Y APARATOS ELÉCTRICOS',
    '#07 INTERRUPTOR O TOMACORRIENTES DEFECTUOSOS O INEXISTENTES',
    '#08 DEFICIENTE PROTECCIÓN CONTRA DESCARGAS ATMOSFÉRICAS Y ESTÁTICAS',
    '#09 DEFICIENTE OPERACIÓN TÉCNICA EN EQUIPOS TECNOLÓGICOS',
    '#10 FALTA DE MANTENIMIENTO O LIMPIEZA DE EQUIPOS Y APARATOS',
    '#11 EXPLOSIÓN',
    '#12 FRICCIÓN O RECALENTAMIENTO DEL MOTOR, MAQUINARIA O APARATOS',
    '#13 INCORRECTA UTILIZACIÓN DE EQUIPOS DE OXICORTE',
    '#14 FUEGO ABIERTO CERCA DE MATERIAL INFLAMABLE',
    '#15 QUEMA DE CAÑAVERALES',
    '#16 COMBUSTIÓN EN ÁREAS YERMAS, BASUREROS Y DESPERDICIOS SÓLIDOS',
    '#17 COMBUSTIÓN EN ÁREAS FORESTALES',
    '#18 EFECTOS PIROTÉCNICOS O DE GUERRA',
    '#19 ARROJAR FÓSFOROS O CIGARROS ENCENDIDOS',
    '#20 TRASIEGO DE GAS',
    '#21 INFLAMACIÓN DE COCINAS',
    '#22 AUTO COMBUSTIÓN',
    '#23 MAL ALMACENAMIENTO DE SUSTANCIAS REACCIONANTES',
    '#24 ACCIDENTES',
    '#25 FENÓMENOS DE LA NATURALEZA',
    '#26 RESIDUOS O DESPRENDIMIENTOS DE LA COMBUSTIÓN',
    '#27 MENORES JUGANDO CON FUEGO',
    '#28 PIROMANÍA',
    '#29 INTENCIONALES',
    '#30 NO DETERMINADOS',
    '#31 SE INVESTIGAN',
    '#32 OTRAS CAUSAS'
    ]

lista_causas_lite = []

for i in range(32): #Llenando la lista ligera de las causas con todos los valores desde causa 1 a causa 32
    lista_causas_lite.append(f"CAUSA #{i+1}")
    

#Creando Variables de Tkinter para los Entries y OptionMenu
comando = StringVar()
comando.set("Comando")
clasificacion = StringVar()
clasificacion.set(lista_clasificaciones[0])
causa = StringVar()
causa.set(lista_causas_lite[15])

#Creando funciones de los botones, etc...


#Creando frames
frame1 = LabelFrame(root)
frame2 = LabelFrame(frame1)
frame3 = LabelFrame(frame1)
frame4 = LabelFrame(frame1)
frame5 = LabelFrame(frame1)
frame6 = LabelFrame(frame1)
frame7 = LabelFrame(frame1)
frame8 = LabelFrame(frame1)
frame9 = LabelFrame(frame1)

#Creando Labels
label1 = Label(frame1, font = ("Tahoma", 15), text = 'Inserte los datos y presione "Narrar"')
label2 = Label(frame2, text = "Comando")
label3 = Label(frame3, text = "Hora Salida")
label4 = Label(frame4, text = "Técnica")
label5 = Label(frame5, text = "Dirección")
label6 = Label(frame6, text = "Consejo Popular")
label7 = Label(frame7, text = "Clasificación")
label8 = Label(frame8, text = "Causa")
label9 = Label(frame9, text = "Hora Entrada")

#Creando Entries y OptionMenus
option_menu1 = OptionMenu(frame2, comando, *lista_comandos) #OptionMenu de Comando
option_menu1.config(width = 12)
entry1 = Entry(frame3, width = 5, bd = 5) #Entry de Hora de salida
entry2 = Entry(frame4, width = 5, bd = 5) #Entry de Tecnica
entry3 = Entry(frame5, width = 38, bd = 5) #Entry de direccion
entry4 = Entry(frame6, width = 20, bd = 5) #Entry de Consejo Popular
option_menu2 = OptionMenu(frame7, clasificacion, *lista_clasificaciones) #OptionMenu de Clasificacion
option_menu2.config(width = 4)
#Este option menu es mas complejo porque necesito enseñar unos valores en el optionMenu pero en realidad devolver otros----------------------
option_menu3 = OptionMenu(frame8, causa, *lista_causas_lite) #OptionMenu de Clasificacion
option_menu3.config(width = 10)#OptionMenu de Causa
for i in range(32):
    option_menu3['menu'].entryconfigure(i, label= lista_causas_full[i]) #Uso este código para cambiar la el nombre de las causas a su nombre completo, pero que aun asi a la hora de mostrarlo en el OpenMenu me siga diciendo solo CAUSA #X


'''
=====================================================================================================================================================
#Dibujando
=====================================================================================================================================================
'''
#Dibujando Labels
label1.grid(row = 0, column = 0, columnspan = 3)
label2.grid(row = 0, column = 0, sticky = W)
label3.grid(row = 0, column = 0, sticky = W)
label4.grid(row = 0, column = 0, sticky = W)
label5.grid(row = 0, column = 0)
label6.grid(row = 0, column = 0, sticky = W)
label7.grid(row = 0, column = 0, sticky = W)
label8.grid(row = 0, column = 0, sticky = W)
label9.grid(row = 0, column = 0, sticky = W)

#Dibujando Frames
frame1.grid(row = 0, column = 0, sticky = W, padx = 5, pady = 10)
frame2.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 2)
frame3.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 2)
frame4.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 2)
frame5.grid(row = 4, column = 0, padx = 5, pady = 2)
frame6.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 2)
frame7.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 2)
frame8.grid(row = 7, column = 0, sticky = W, padx = 5, pady = 2)
frame9.grid(row = 8, column = 0, sticky = W, padx = 5, pady = 2)

#Dibujando Entries y OptionMenus
option_menu1.grid(row = 0, column = 1, padx = (145, 5))
entry1.grid(row = 0, column = 1, padx = (185, 48))
entry2.grid(row = 0, column = 1, padx = (213, 48))
entry3.grid(row = 1, column = 0, padx = (11, 12), pady = 3)
entry4.grid(row = 0, column = 1, padx = (58, 5))
option_menu2.grid(row = 0, column = 1, padx = (199, 5))
option_menu3.grid(row = 0, column = 1, padx = (189,5))


root.mainloop()


























