# importar todos los elementos y funciones de tkinter
from tkinter import *


# SECCION DE FUNCIONES / LOGICA
def encriptar():
    # obtener texto de tkinter de la entrada texto_original
    texto_a_encriptar = texto_original.get() 

    # obtener texto de tkinter de la entrada llave
    llave_encriptar = llave.get()

    # inicializar variable para ir guardando cada letra del texto encriptado
    texto_encriptado = ''

    for letra in texto_a_encriptar.upper(): # iterar sobre cada letra del texto
        indice = alfanumerico.index(letra) # obtener el indice/posicion de la letra
        nuevo_indice = indice + int(llave_encriptar) # sumarle la llave a la posicion original
        
        # volver a iniciar cuenta desde 0 en caso de ser necesario
        if nuevo_indice >= 37: 
            nuevo_indice -= 37

        # ir sumandole cada letra a nuestra variable de texto_encriptado
        texto_encriptado += alfanumerico[nuevo_indice] 

    # configurar el texto de tkinter para mostrar nuesto texto encriptado
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

# inicializar tkinter
ventana = Tk()

titulo = Label(ventana, text='Encripcion Cesar')
titulo.grid(row=0, column=0)

# SECCION DE ENTRADAS DE TEXTO
texto_original_label = Label(ventana, text='Escribe el texto:')
texto_original = Entry(ventana)

texto_original_label.grid(row=1, column=0)
texto_original.grid(row=1, column=1)

llave_label = Label(ventana, text='Escribe la llave: ')
llave = Entry(ventana)

llave_label.grid(row=2, column=0)
llave.grid(row=2, column=1)

# SECCION DE BOTONES
boton_encriptar = Button(ventana, text='Encriptar', command=encriptar)
boton_desencriptar = Button(ventana, text='Desencriptar', command=desencriptar)

boton_encriptar.grid(row=3, column=0)
boton_desencriptar.grid(row=3, column=1)

# SECCION DE RESULTADO
resultado_label = Label(ventana, text='Resultado:')
resultado_texto = Label(ventana, text='')

resultado_label.grid(row=4, column=0)
resultado_texto.grid(row=5, column=0)

ventana.mainloop()
