# Declara los personajes usados en el juego como en el ejemplo:

define M = Character("???")
define Paoli = Character("Rodolfo De Paoli")
define Aficcion = Character("Aficion")
image Messi parado = "Messi_parado.png"
image Estadio = "Estadio.png"
# El juego comienza aquí.
transform terremoto:
    linear 0.05 xoffset 5 yoffset -5
    linear 0.05 xoffset -5 yoffset 5
    linear 0.05 xoffset 3 yoffset -3
    linear 0.05 xoffset -3 yoffset 3
    linear 0.05 xoffset 0 yoffset 0
    repeat 
label start:

    scene Estadio



    "El estadio estaba más lleno que nunca, sería el primer partido de la selección argentina en el mundial, en esta ocasión se enfrentaría a la selección de Arabia Saudita. Al ver a los jugadores de Argentina ingresar al campo, la multitud se enloqueció."
    
    
    scene Estadio at terremoto
    Paoli "¡Los jugadores de Argentina ingresan al estadio! Se espera una victoria firme por parte de la selección argentina, que llega con una racha de 36 victorias consecutivas desde el 6 de julio de 2019”."

    

    

    # Finaliza el juego:

    return
