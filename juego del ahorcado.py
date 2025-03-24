from random import choice

palabras = ['consejero', 'dinosaurio', 'helicoptero', 'desayuno', 'emprendedor']
letras_correctas = []
letras_incorrectas = []
intentos = 6
respuestas_correctas = 0
fin_juego = False

def elegir_palabra(lista_de_palabras):
    palabra_elegida = choice(lista_de_palabras)
    letras_diferentes = len(set(palabra_elegida))

    return palabra_elegida, letras_diferentes

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Por favor, elige una letra")

        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida

def mostrar_tablero_nuevo(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def comprobar_letra(letra_elegida, palabra_oculta, intentos, aciertos):
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        aciertos += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra, prueba con otra")
    else:
        letras_incorrectas.append(letra_elegida)
        intentos -= 1

    if intentos == 0:
        fin = perder()
    elif aciertos == letras_unicas:
        fin = ganar(palabra_oculta)

    return intentos, fin, aciertos

def perder():
    print("No te quedan intentos")
    print("La palabra oculta era " + palabra)

    return True

def ganar(palabra_descubierta):
    mostrar_tablero_nuevo(palabra_descubierta)
    print("¡Felicidades, adivinaste la palabra!!!")

    return True

palabra, letras_unicas = elegir_palabra(palabras)

while not fin_juego:
    print('\n' + '*' * 20 + '\n')
    mostrar_tablero_nuevo(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Intentos: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()
    intentos, fin, respuestas_correctas = comprobar_letra(letra, palabra, intentos, respuestas_correctas)
    fin_juego = fin
