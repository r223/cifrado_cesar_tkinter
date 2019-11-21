from tkinter import *


# SECCION DE FUNCIONES / LOGICA
def encriptar():
    texto_a_encriptar = texto_original.get() 
    llave_encriptar = llave.get()
    texto_encriptado = ''

    for letra in texto_a_encriptar.upper(): 
        indice = alfanumerico.index(letra)
        nuevo_indice = indice + int(llave_encriptar)
        
        if nuevo_indice >= 37: 
            nuevo_indice -= 37

        texto_encriptado += alfanumerico[nuevo_indice] 

    resultado_texto.configure(text=texto_encriptado)


def desencriptar():
    texto_a_desencriptar = texto_original.get()
    llave_desencriptar = llave.get()

    texto_desencriptado = ''

    for letra in texto_a_desencriptar.upper(): 
        indice = alfanumerico.index(letra) 
        nuevo_indice = indice - int(llave_desencriptar)
        texto_desencriptado += alfanumerico[nuevo_indice]

    resultado_texto.configure(text=texto_desencriptado)


# crear lista con abecedario y numeros
alfanumerico = list('ABCDEFGHIJKLMNOPQRSTUVWYXZ1234567890 ')


# SECCION DE TKINTER
ventana = Tk() # inicializar tkinter
ventana.wm_title('Encripcion y Desencriptacion')
ventana.geometry('707x440')
ventana.configure(bg='gray20')

titulo = Label(ventana, text='Encriptador Cesar')
titulo.configure(font=('Times New Roman', 40), bg='gray20', fg='goldenrod')
titulo.grid(row=0, column=0, columnspan=2, sticky='NESW')

autor = Label(ventana, text='Nombre aqui')
autor.configure(font=('Helvetica', 14), bg='gray20', fg='goldenrod')
autor.grid(row=1, column=0, columnspan=2, sticky='NESW')

# espaciador vacio
Frame(ventana, bg='gray20').grid(row=2, column=0 ,columnspan=2,pady=20)

# SECCION DE ENTRADAS DE TEXTO
texto_original_label = Label(ventana, text='Escribe el texto:')
texto_original_label.configure(font=('Helvetica', 28), bg='gray20', fg='forest green')
texto_original_label.grid(row=3, column=0)

texto_original = Entry(ventana)
texto_original.configure(font=('Helvetica', 28), bg='gray97')
texto_original.grid(row=3, column=1)

llave_label = Label(ventana, text='Escribe la llave:')
llave_label.configure(font=('Helvetica', 28), bg='gray20', fg='forest green')
llave_label.grid(row=4, column=0)

llave = Entry(ventana)
llave.configure(font=('Helvetica', 28), bg='gray97')
llave.grid(row=4, column=1)

# espaciador vacio
Frame(ventana, bg='gray20').grid(row=5, column=0 ,columnspan=2,pady=20)

# SECCION DE BOTONES
boton_encriptar = Button(ventana, text='  Encriptar ', command=encriptar)
boton_encriptar.configure(
    font=('Helvetica', 28), bg='gray12', highlightbackground='gold', fg='gold'
)
boton_encriptar.grid(row=6, columnspan=1, column=0, sticky='NESW')

boton_desencriptar = Button(ventana, text='Desencriptar', command=desencriptar)
boton_desencriptar.configure(
    font=('Helvetica', 28), bg='gray12', highlightbackground='dodger blue', fg='dodger blue'
)
boton_desencriptar.grid(row=6, columnspan=1, column=1, sticky='NESW')

# espaciador vacio
Frame(ventana, bg='gray20').grid(row=7, column=0 ,columnspan=2,pady=10)

# SECCION DE RESULTADO
resultado_label = Label(ventana, text='Resultado:')
resultado_label.configure(font=('Helvetica', 24), bg='gray20', fg='red3')
resultado_label.grid(row=8, column=0, columnspan=2,sticky='NESW')

resultado_texto = Label(ventana, text='')
resultado_texto.configure(font=('Helvetica', 28), bg='gray18', fg='lawn green')
resultado_texto.grid(row=9, column=0, columnspan=2, sticky='NESW')


ventana.mainloop()