## Personajes #######################################################

define M = Character("???")
define Paoli = Character("Rodolfo De Paoli")
define Aficion = Character("Aficion")


## Sprites  #######################################################

image Messi parado = "Messi_parado.png"
image Francisco = "Francisco.png"

## Escenarios #######################################################
image Estadio = "Estadio.png"
image Comentarista = "Comentarista.png"
image Corredor = "Corredor.png"
image Cancha esquina = "Cancha_esquina.png"
image AR vs ARABIA = "Introduccion Arabia vs argentina.png"

## transforms/funciones #######################################################
define flash_wakeup = Fade(0.1, 0.3, 0.8, color="#fff")
# Definimos la transición
transform entrar_izquierda:
    xalign -0.5 yalign 1.0  # Empieza fuera de la pantalla a la derecha
    easein 0.5 xalign 0.1  # Se mueve suavemente hacia la izquierda (ajusta el 0.8 a tu gusto)
transform sprite_cansado:
    yoffset 20
    
    block:
        easein 1.0 yoffset 40  # Se agacha un poco más al exhalar (lento)
        easeout 1.0 yoffset 0 # Sube a su posición cansada al inhalar
        repeat
    
transform terremoto:
    linear 0.05 xoffset 5 yoffset -5
    linear 0.05 xoffset -5 yoffset 5
    linear 0.05 xoffset 3 yoffset -3
    linear 0.05 xoffset -3 yoffset 3
    linear 0.05 xoffset 0 yoffset 0
    repeat 

transform dim:
    linear 0.3 matrixcolor BrightnessMatrix(-0.5)
transform focus:
    linear 0.3 matrixcolor BrightnessMatrix(0.0)


label start:

    play music "Default.mp3" fadein 1.0 volume 0.1
    play sound "Aficion_bucle.ogg" fadein 1.0 volume 0.18 loop
    scene Estadio



    "El estadio estaba más lleno que nunca, sería el primer partido de la selección argentina en el mundial, en esta ocasión se enfrentaría a la selección de Arabia Saudita. Al ver a los jugadores de Argentina ingresar al campo, la multitud se enloqueció."
    scene Comentarista
    Paoli "¡Los jugadores de Argentina ingresan al estadio! Se espera una victoria firme por parte de la selección argentina, que llega con una racha de 36 victorias consecutivas desde el 6 de julio de 2019”."

    scene Estadio with flash_wakeup
    
    pause 0.4

    scene Estadio at terremoto
    play sound "Aficion_EX.ogg" fadein 0.1 volume 0.25
    Aficion"¡Oooh eeeh, oooh eeeh, oooh eeeh, oooh eeeh!"

    stop sound fadeout 0.1
    play sound "Aficion_bucle.ogg" volume 0.18 loop
    scene Comentarista
    Paoli "La Afición está completamente extasiada con la llegada de los jugadores a la cancha"
    
    scene Corredor with wipeleft
    show Messi parado:
                xalign 1.0
                yalign 1.0
    with dissolve

    M "Este es solo el comienzo de mi último mundial… voy a darlo TODO"

    scene AR vs ARABIA with fade
    
    stop sound fadeout 0.1
    "Ambos equipos se posicionaron en el centro del campo para cantar sus respectivos himnos nacionales."
    stop music fadeout 1.0
   
    play music "Himno_argentino.mp3" fadein 1.0 volume 0.3
    "El estadio entero quedó en silencio mientras sonaban las canciones patrias y las cámaras enfocaban a los jugadores, que mostraban concentración y emoción en sus rostros."
    stop music fadeout 1.0



    scene Comentarista at terremoto

    Paoli "¡Arrancó el partido!"

    scene Comentarista

    Paoli " Argentina ya mueve la pelota y la controla perfectamente, tocando de un lado al otro mientras busca un hueco para atacar. Es nuestra selección la que empieza dominando estos primeros minutos del encuentro"
    scene Cancha esquina
    show Messi parado at sprite_cansado:
            entrar_izquierda
        

    M "Sighh… bien, tenemos la pelota"


    return
