print('***** ENCRIPCION CESAR *****\n')

alfanumerico = list('ABCDEFGHIJKLMNOPQRSTUVWYXZ1234567890 ')

texto_original = input('Escribe tu texto aqui: \n').upper()
llave = input('\nEscribe tu llave aqui (Numero entre 0 y 36): \n')

texto_encriptado = ''

for letra in texto_original: 
    indice = alfanumerico.index(letra) 

    nuevo_indice = indice + int(llave)
    
    if nuevo_indice >= 37:
        nuevo_indice -= 37

    texto_encriptado += alfanumerico[nuevo_indice]


# imprimir resultado
print('\nEl resultado de tu texto encriptado es: "' + texto_encriptado + '"\n\n')


desencriptar_respuesta = input('Deseas desencriptar un texto?: ').lower()
texto_decriptado = ''

if desencriptar_respuesta == 'si':    
    llave_d = input('Escribe la llave para desencriptar: \n')
    texto_d = input('Escribe el texto que quieres desencriptar: \n').upper()

    for letra in texto_d:
        indice = alfanumerico.index(letra)
        nuevo_indice = indice - int(llave)

        texto_decriptado += alfanumerico[nuevo_indice]

print('\nEl resultado de la decodificacion es: ' + texto_decriptado)





