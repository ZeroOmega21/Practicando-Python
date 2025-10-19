import tkinter as tk
#crea el objeto de la ventana principal
root = tk.Tk()

#configuraciones de la ventana
root.title("Tk Example")
root.configure(bg="lightblue")    #background color
root.minsize(200,200)               #ancho y alto minimo
root.maxsize(500,500)               #ancho y alto maximo
root.geometry("300x300+50+50")      #ancho x alto + posicion x + posicion y

#crear labels
# 'root' es la ventana principal de la aplicación
# 'grid' es un método para organizar el widget en la ventana
tk.Label(root, text="Hola a todos. probando TKinter").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="- ZeroOmega21").grid(row=1, column=0, columnspan=2)



#Boton
root.title("Boton Example")                                                     #titulo de la ventana
Boton = tk.Button(root,text="Cerrar ventana", width=25, command=root.destroy)   #crea un boton que cierra la ventana al ser presionado
Boton.grid(row=2, column=0, columnspan=2)                                       #posiciona el boton en la ventana

#Campos de entrada de texto

form_frame = tk.Frame(root)             # crea un frame para contener los elementos del formulario 
form_frame.grid(row=3, column=0, columnspan=2, pady=10)  # grid el frame en root con 10 pixeles de espacio vertical

tk.Label(form_frame, text="Ingrese su nombre:").grid(row=0, column=0, sticky="w")   # etiqueta para el campo de nombre -- #sticky="w" alinea el texto a la izquierda
tk.Label(form_frame, text="Ingrese su edad:").grid(row=1, column=0, sticky="w")     # etiqueta para el campo de edad    
Elemento1 = tk.Entry(form_frame)                                                    # campo de entrada para el nombre
Elemento2 = tk.Entry(form_frame)                                                    # campo de entrada para la edad 
Elemento1.grid(row=0, column=1)                                                     # posiciona el campo de nombre en la fila 0, columna 1
Elemento2.grid(row=1, column=1)                                                     # posiciona el campo de edad en la fila 1, columna 1

#Boton de Check
Dato1 = tk.IntVar()                             #variable para almacenar el estado del CheckButton
tk.Checkbutton(root, text="hombre",  variable=Dato1).grid(row=4, column=0)  #crea un CheckButton para seleccionar "hombre")
Dato2 = tk.IntVar()                             #variable para almacenar el estado del CheckButton
tk.Checkbutton(root, text="mujer",  variable=Dato2).grid(row=4, column=1)  #crea un CheckButton para seleccionar "mujer")

root.mainloop()                     #mantiene la ventana abierta 
