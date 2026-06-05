## Personajes #######################################################

define M = Character("???")
define Paoli = Character("Rodolfo De Paoli")
define Aficion = Character("Aficion")
define LP = Character("Leandro Paredes")

## Sprites  #######################################################

image Messi parado = "Messi_parado.png"
image Francisco = "Francisco.png"
image jugador argentina = "Jugador_argentina.png"
image j arabia = "Jugador_arabia.png"
image ju polonia = "Jugador_polonia.png"
image ja mexico = "Jugador_mexico.png"


## Escenarios #######################################################
image Estadio = "Estadio.png"
image Comentarista = "Comentarista.png"
image Corredor = "Corredor.png"
image Cancha esquina = "Cancha_esquina.png"
image AR vs ARABIA = "Introduccion Arabia vs argentina.png"
image black = "Black.png"

## transforms/funciones #######################################################
define flash_wakeup = Fade(0.1, 0.3, 0.8, color="#fff")
# Definimos la transición
transform entrar_izquierda:
    xalign -0.5 yalign 1.0  # Empieza fuera de la pantalla a la derecha
    easein 0.5 xalign 0.1  # Se mueve suavemente hacia la izquierda (ajusta el 0.8 a tu gusto)
transform irse_derecha_caminando:
    xalign 0.1 yalign 1.0  # Empieza fuera de la pantalla a la derecha
    easein 0.5 xalign 1.5  # Se mueve suavemente hacia la izquierda (ajusta el 0.8 a tu gusto)
transform sprite_cansado:
    yoffset 20
    
    block:
        easein 1.0 yoffset 40  # Se agacha un poco más al exhalar (lento)
        easeout 1.0 yoffset 0 # Sube a su posición cansada al inhalar
        repeat

transform terremotoCorto:
    linear 0.05 xoffset 5 yoffset -5
    linear 0.05 xoffset -5 yoffset 5
    linear 0.05 xoffset 3 yoffset -3
    linear 0.05 xoffset -3 yoffset 3
    linear 0.05 xoffset 0 yoffset 0
    repeat 10

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

    play music "Default.mp3" fadein 1.0 volume 0.3 loop
    play sound "Aficion_bucle.ogg" fadein 1.0 volume 0.18 loop
    scene Estadio



    "El estadio estaba más lleno que nunca, sería el primer partido de la selección argentina en el mundial, en esta ocasión se enfrentaría a la selección de Arabia Saudita."
    "Al ver a los jugadores de Argentina ingresar al campo, la multitud se enloqueció."
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



    scene Comentarista at terremoto with fade

    Paoli "¡Arrancó el partido!"

    scene Comentarista

    Paoli " Argentina ya mueve la pelota y la controla perfectamente, tocando de un lado al otro mientras busca un hueco para atacar. Es nuestra selección la que empieza dominando estos primeros minutos del encuentro"
    scene Cancha esquina



    play music "Tema_futbol2.mp3" fadein 1.0 volume 0.4 loop









    show Messi parado at sprite_cansado, focus:
            entrar_izquierda
    play sound "Pasos.ogg" volume 0.5

    M "Sighh… bien, tenemos la pelota"

    play sound "Pasos.ogg" volume 0.5

    show Messi parado at irse_derecha_caminando
    
    
    Paoli "Argentina juega a lo seguro, moviendo la pelota con tranquilidad y esperando el momento justo para acelerar. La selección de Arabia Saudita se mete toda atrás tratando de cerrar espacios"
    
    scene Cancha esquina:
        zoom 1.2
    
    "Tras unos minutos Papu Gómez recibe el balón cerca de la banda izquierda y levanta la cabeza."

    show Messi parado at entrar_izquierda
    play sound "Pasos.ogg" volume 0.5
    pause 0.5
    show jugador argentina:
        xalign 0.2 yalign 1.0  
        easein 0.7 xalign 1.5
    
    
    
    

    Paoli "¡Atención que la tiene el Papu Gómez! ¡Encontró un espacio, se mete al área, esta jugada puede ser peligrosa!"
    

    "El argentino comienza a correr entre los defensores, intentando penetrar el área rival, pero justo antes de rematar aparece Saud Abdulhamid."
    hide jugador argentina  
    hide Messi parado
    scene Cancha esquina:
        truecenter
    with flash_wakeup

    play sound "Chocar.ogg" volume 1
    show jugador argentina:
        xalign -0.5 yalign 1.0
        easein 0.2 xalign 0.1 yalign 1.0



    show j arabia:
        xalign 0.8 yalign 1.0
        easein 0.1 xalign 0.15 yalign 1.0
   

    

    Paoli "¡Qué cierre de Abdulhamid! Justo al límite logra desviar la pelota y será tiro de esquina para Argentina. Primer aviso serio de la selección argentina en el partido"
    
    scene Cancha esquina with dissolve

    show Messi parado at Transform(xalign=0.1, yalign=1.0)

    M "Qué buena oportunidad… no la desperdiciaré"

    play sound "Pelotazo.mp3" volume 1
    show Messi parado at Transform(xalign=0.1, yalign=1.0):
        easein 0.2 xalign 0.2 yalign 0.8
        easeout 0.5 xalign 0.1 yalign 1.0

    Paoli "¡Se viene el tiro de esquina para Argentina! La pelota ya está en el aire, viajando directo al área… ¡puede llegar el primero del partido!"

    scene Cancha esquina:
        zoom 1.3 
    hide j arabia

    show j arabia:
        xalign 0.3 
        yalign 1.0

    play sound "Impresion.mp3" fadein 0.1 volume 0.8
    show jugador argentina:
        easein 0.2 xalign 0.2 yalign 1.0
        easeout 0.5 xalign 0.2 yalign 0.8
        easein 0.2  xalign 0.2 yalign 1.0
        terremotoCorto

    "Mientras todos los jugadores saltaban buscando conectar el balón, Saud Abdulhamid sujetó claramente a Leandro Paredes justo cuando este intentaba elevarse para cabecear."
    
    scene Comentarista
    Paoli "¡Epa, atención! Paredes cayó dentro del área y los jugadores argentinos están reclamando desesperadamente. Parece que Abdulhamid lo agarró cuando iba a saltar"
    "El árbitro observó la jugada por unos segundos mientras todo el estadio quedaba en tensión. Tras escuchar las insistentes protestas de los jugadores argentinos, decidió llevar la acción al VAR."
    "Atención porque el árbitro va a revisar la jugada! Todo el estadio está expectante… esto puede terminar en penal para Argentina"
    "Las pantallas gigantes mostraban la repetición dejando en evidencia cómo Saud Abdulhamid sujetaba a Leandro Paredes dentro del área."
    "Después de unos segundos eternos, el VAR confirmó la infracción."

    scene Comentarista at terremoto
    play sound "Aficion_EX.ogg" volume 0.5
    Paoli "¡Penal,Penal para Argentina! El árbitro marca el punto penal y la selección argentina tiene la chance de abrir el marcador"

    scene Cancha esquina with wipeleft

    LP "Dale vos sabés" 

    "Papu Gómez soltó una pequeña risa y se chocó las manos con sus compañeros."

    "Incluso desde el banco podrían verse gestos de tranquilidad, porque todos sabían que, si alguien podía convertir ese penal en gol, era él"

    show Messi parado at Transform(xalign=0.1, yalign=1.0)

    "Respiré lentamente mientras me preparaba para patear. Escuchaba el ruido ensordecedor de los hinchas alentando desde las tribunas, pero en ese momento solo podía concentrarme en una cosa: el balón."


    "El estadio entero quedó en silencio por unos segundos.Tomé carrera y golpeé la pelota." 
    play sound "Pelotazo.mp3" volume 1.5
    show Messi parado at Transform(xalign=0.1, yalign=1.0):
        easein 0.2 xalign 0.2 yalign 0.8
        easeout 0.5 xalign 0.1 yalign 1.0
    "Todo parecía ir en cámara lenta mientras el balón viajaba hacia el arco y el arquero se lanzaba intentando detenerlo."

    "Miles de personas contenían la respiración esperando el resultado de la jugada."

    "Hasta que finalmente la pelota cruzó la línea."

    scene estadio with flash_wakeup:
        terremoto

# ... (Viene del gol de penal)
    play sound "Aficion_EX.ogg" volume 0.7
    Aficion "¡¡¡GOOOOOOOOOOOL!!!"

    Paoli "¡Gol de Argentina!  La selección argentina empieza ganando el partido y el estadio explota completamente de emoción."

    show Messi parado at focus:
        xalign 0.1 yalign 1.0
    M "Sighh... empezamos ganando, mantengamos esta racha chicos."

# --- CONTINUACIÓN DEL PARTIDO: ARABIA SAUDITA ---

    scene Cancha esquina with dissolve
    "Ahora la selección de Arabia Saudita tenía el balón. Intentaban avanzar por el mediocampo, pero tras una mala jugada Argentina logró recuperar la posesión con facilidad."

    scene Comentarista
    Paoli "¡Argentina vuelve a controlar el partido, tocando la pelota con tranquilidad y buscando ampliar la ventaja!"

    scene Cancha esquina
    "Mientras la selección argentina intentaba mantener la posesión para ampliar la ventaja, un pase quedó mal dirigido y Saleh Al-Shehri aprovechó el descuido para interceptar el balón."
    
    show j arabia at entrar_izquierda
    "Inmediatamente comenzó el contraataque saudí. Al-Shehri avanzó rápidamente mientras la defense argentina retrocedía intentando reorganizarse."

    scene Comentarista at terremoto
    Paoli "¡Atención con Arabia Saudita! ¡Recuperaron la pelota y salen rápido a la contra!"

    scene Cancha esquina with flash_wakeup
    show j arabia:
        xalign 0.1 yalign 1.0
        easein 0.3 xalign 0.5
    show jugador argentina:
        xalign 0.8 yalign 1.0
        easein 0.4 xalign 1.2 # Defensa retrocediendo
    "El delantero saudí siguió avanzando, logró acomodarse dentro del área y sacó un remate cruzado que terminó entrando junto al palo, marcando así el empate para Arabia Saudita."

    hide j arabia
    hide jugador argentina
    scene Comentarista
    Paoli "¿Qué ha pasado con Argentina? Hubo un descuido que terminó generando una oportunidad clarísima para Arabia Saudita."
    Paoli "El partido empezó totalmente dominado por la selección argentina, pero ahora todo cambió. ¿Cómo se desarrollará este encuentro?"

    scene Cancha esquina with dissolve
    show jugador argentina at focus:
        xalign 0.2 yalign 1.0
    show j arabia at dim:
        xalign 0.8 yalign 1.0
    "Tras recuperar el balón, Argentina intentó salir rápidamente al contraataque en varias ocasiones. Ángel Di María y Julián Álvarez buscaron penetrar la defensa saudí con velocidad y pases rápidos..."
    "Pero cada intento fue detenido por los defensores rivales y por las grandes intervenciones del arquero saudí."

    scene Comentarista
    Paoli "Argentina sigue intentando, pero Arabia Saudita se está defendiendo muy bien. La defensa está firme y no deja espacios."

    scene Cancha esquina
    hide jugador argentina
    hide j arabia
    "Sin embargo, Arabia Saudita volvió a recuperar la pelota y salió rápidamente hacia el ataque."

    scene Comentarista at terremoto
    Paoli "¡Arabia Saudita está atacando de nuevo! ¿Qué está pasando con la defensa argentina? ¡Hay muchísimos espacios!"

    scene Cancha esquina:
        zoom 1.2
    play sound "Pelotazo.mp3" volume 1
    show j arabia:
        xalign -0.2 yalign 1.0
        easein 0.5 xalign 0.5
        easein 0.2 xalign 0.2 yalign 0.8
        easeout 0.5 xalign 0.1 yalign 1.0
    "Saleh Al-Shehri avanzó a toda velocidad, dejando atrás a los defensores argentinos hasta quedar frente al arco. Sin dudarlo, remató con precisión y envió la pelota al fondo de la red."

    scene Estadio at terremoto
    play sound "Aficion_EX.ogg" volume 0.3
    Aficion "¡¡¡GOOOOOOOOOOOL!!!"

    scene Comentarista
    Paoli "¡Gol de Arabia Saudita! ¡Increíble remontada! El partido ahora está 2-1 a favor de Arabia Saudita y el estadio entero no puede creer lo que acaba de pasar."

    $ salem = Character("Salem Al-Dawsari", color="#006c35")
    salem "هيا، إذا لم يفوزوا سينفد النفط لديهم."

    scene Cancha esquina with dissolve
    "Argentina intentó presionar durante todo el partido para conseguir el empate, pero la defensa saudí se mantenía firme y defendía de manera impecable cada ataque argentino."

    show Messi parado at sprite_cansado, focus:
        xalign 0.5 yalign 1.0
    M "Debo hacerlo… tengo que hacerlo."

    scene Comentarista
    Paoli "Argentina sigue atacando, pero Arabia Saudita está resistiendo todo. Cada avance argentino termina siendo bloqueado por la defensa o por el arquero rival."

    scene Cancha esquina
    show Messi parado at sprite_cansado, dim:
        xalign 0.1 yalign 1.0
    show jugador argentina at focus:
        xalign 0.5 yalign 1.0
    "Ángel Di María intentó desbordar por la banda, Julián Álvarez buscó espacios dentro del área y hasta Lionel Messi trató de generar peligro con pases y remates, pero todos los ataques eran detenidos una y otra vez."
    "Así avanzó el partido. Cada minuto se volvía más importante y la tensión aumentaba en todo el estadio."
    "Finalmente, el árbitro observó su reloj y llevó el silbato a su boca."
    
    scene Estadio with flash_wakeup
    stop music fadeout 1.0
    "*(Piiiiiiiiiiip)*"
    play music "Default.mp3" fadein 1.0 volume 0.4 loop
    
    scene Comentarista
    Paoli "¡Final del partido! Argentina perdió… ¡Ha ganado Arabia Saudita! ¡Sorpresa total en el mundial!"

    scene Estadio with dissolve
    "Todo el sector argentino quedó en silencio tras la derrota. Algunos aficionados bajaban la cabeza mientras otros miraban el campo sin poder creer lo ocurrido."

    $ federico = Character("Federico", color="#eccc68")
    $ dimas = Character("Dimas", color="#ff7f50")
    
    federico "Perdimos…"
    dimas "Perdimos…."

    scene Corredor with dissolve
    show Messi parado at sprite_cansado, focus:
        xalign 0.5 yalign 1.0
    "Después de aquella derrota, la selección argentina abandonó el campo completamente devastada. Los jugadores caminaban lentamente hacia el túnel con la mirada perdida, sin poder creer lo que acaba de ocurrir."
    "El estadio entero estaba sorprendido por la inesperada victoria de Arabia Saudita. Mientras la afición saudí celebraba eufóricamente, del lado argentino solo se escuchaba silencio."
    
    show Messi parado at sprite_cansado:
        easein 1.0 xalign 0.3
    "El capitán permanecía serio, observando el suelo por unos segundos antes de retirarse."

    scene Comentarista
    Paoli "Nadie puede creer este resultado. Argentina llegó como una de las grandes favoritas del mundial y hoy se va derrotada en su debut."

    scene Corredor
    show Messi parado at sprite_cansado, focus:
        xalign 0.3 yalign 1.0
    M "Esto… esto no puede ser cierto. Nosotros debimos haber ganado… no volveré a perder, cueste lo que cueste."


    # --- ESCENA 2: EL RESURGIR CONTRA MÉXICO ---

    scene black with fade
    "Después de la dolorosa derrota contra la selección de Arabia Saudita, la selección argentina pasó varios días entrenando intensamente y corrigiendo errores."
    "El ambiente dentro del equipo seguía siendo tenso, pero ahora los jugadores estaban más decididos que nunca a recuperarse."

    scene Estadio with flash_wakeup
    play sound "Aficion_bucle.ogg" volume 0.15 loop
    "Llegó el día del enfrentamiento contra la selección de México. Desde el comienzo del partido podía sentirse la presión en ambos equipos, ya que una derrota podía complicar seriamente las posibilidades de clasificar."

    scene Comentarista
    Paoli "¡Argentina sabe que hoy no puede fallar! Después del golpe sufrido contra Arabia Saudita, necesita una victoria para volver a meterse en pelea."

    scene Cancha esquina with dissolve
    show jugador argentina at focus:
        xalign 0.2 yalign 1.0
    show ja mexico at dim:
        xalign 0.8 yalign 1.0
    "Durante el primer tiempo, México defendió con mucha intensidad. Argentina dominaba la posesión, pero le costaba encontrar espacios claros. Ángel Di María intentó generar peligro por la banda derecha..."
    
    show Messi parado at entrar_izquierda
    show jugador argentina at dim
    "La primera gran oportunidad llegó cuando Lionel Messi recibió el balón fuera del área. Levantó la cabeza y sacó un potente remate que pasó apenas desviado del arco mexicano."

    scene Comentarista
    Paoli "¡Uhhh, avisó! Argentina empieza a acercarse cada vez más."

    scene Cancha esquina
    hide jugador argentina
    hide ja mexico
    show Messi parado at focus:
        xalign 0.1 yalign 1.0
    "Con el paso de los minutos, la tensión aumentaba. Sin embargo, en el segundo tiempo apareció el momento que cambiaría el partido."
    "Ángel Di María tocó hacia el centro para el capitán, quien avanzó unos metros..."
    
    play sound "Pelotazo.mp3" volume 1.5
    show Messi parado:
        easein 0.3 xalign 0.4 yalign 0.9
        easeout 0.2 xalign 0.3 yalign 1.0
    "...y, desde afuera del área, sacó un remate preciso y raso que terminó entrando junto al palo."

    scene Estadio at terremoto
    play sound "Aficion_EX.ogg" volume 0.3
    Aficion "¡¡¡GOOOOOOOOOOOL!!!"

    scene Comentarista
    Paoli "¡Gol de Argentina! ¡Apareció el capitán cuando más lo necesitaba la selección!"

    scene Cancha esquina with dissolve
    hide Messi parado
    show jugador argentina at focus:
        xalign 0.3 yalign 1.0
    show ja mexico at dim:
        xalign 0.7 yalign 1.0
    "Tras el primer gol, Argentina ganó confianza y comenzó a dominar completamente el encuentro. México intentó adelantarse buscando el empate, pero eso dejó espacios atrás."
    "En los últimos minutos, un tiro de esquina terminó con la pelota en los pies de... ¡Enzo Fernández! El mediocampista amagó dentro del área y sacó un remate colocado imposible para el arquero mexicano."

    scene Estadio at terremoto
    play sound "Aficion_EX.ogg" volume 0.3
    Aficion "¡¡¡GOOOOOOOOOOOL!!!"

    scene Comentarista
    Paoli "¡Golazo de Enzo Fernández! ¡Argentina liquida el partido y vuelve a sonreír en el mundial!"

    scene Estadio with flash_wakeup
    "El árbitro marcó el final del encuentro y los jugadores argentinos celebraron con alivio."

    scene Comentarista
    Paoli "¡Argentina ha ganado 2-0 contra México! La selección consigue recuperarse después de la dura derrota frente a Arabia Saudita y mantiene vivo el sueño mundialista."

    scene Corredor with dissolve
    show Messi parado at focus:
        xalign 0.5 yalign 1.0
    M "Esto no parará aquí."

    $ M = Character("Messi")
    $ entrevistador = Character("Entrevistador", color="#a4b0be")

    entrevistador "Después de esta importante victoria… ¿tenés algo para decir sobre este partido y sobre los encuentros que están por venir?"

    show Messi parado:
        easein 0.2 yoffset 10
    M "Sabíamos que teníamos que responder después de la derrota contra Arabia Saudita. Fueron días muy difíciles para nosotros, porque no esperábamos empezar el mundial de esa manera. Pero este grupo nunca dejó de confiar en sí mismo."

    "El capitán respiró profundamente mientras observaba a los hinchas argentinos celebrando en las tribunas."

    M "Hoy demostramos que estamos más unidos que nunca. Sabíamos que no podíamos fallar y salimos a jugar cada pelota como si fuera la última. Todavía queda mucho camino por recorrer, pero esta victoria nos devuelve la confianza."
    
    M "La gente siempre estuvo con nosotros, incluso en los momentos más difíciles. Vamos a seguir luchando hasta el final por este sueño. Cada partido será una final para nosotros."

    scene Comentarista
    Paoli "Se nota el alivio en Messi y en toda la selección argentina. Después del golpe sufrido en el debut, este triunfo vuelve a encender la ilusión de todo un país."


    # --- ESCENA 3: DEFINICIÓN CONTRA POLONIA ---

    scene black with fade
    "El último partido de la fase de grupos se disputaba contra la selección de Polonia. Ambos equipos se encontraban tensos, preparándose para definir quién avanzaría a los octavos de final del mundial."
    "Desde el inicio del encuentro, la selección argentina tomó el control del balón, moviéndolo con paciencia mientras buscaba generar un contraataque peligroso contra la defensa polaca."

    scene Comentarista
    Paoli "Argentina domina la posesión en estos primeros minutos, pero Polonia se defiende muy bien y no deja espacios."

    scene Cancha esquina with dissolve
    show Messi parado at dim:
        xalign 0.1 yalign 1.0
    show jugador argentina at focus:
        xalign 0.5 yalign 1.0
    show ju polonia at dim:
        xalign 0.8 yalign 1.0
    "Durante gran parte del primer tiempo, Argentina atacó constantemente. Messi intentó crear oportunidades con pases filtrados, mientras Ángel Di María buscaba romper por la banda derecha. Sin embargo, la defensa polaca y el arquero Wojciech Szczęsny lograron mantener el empate."

    show Messi parado at focus
    show jugador argentina at dim
    M "Dale, sigamos presionando, los espacios van a aparecer."

    $ DePaul = Character("Rodrigo De Paul", color="#74b9ff")
    DePaul "Tranquilos, no dejemos de mover la pelota."

    show Messi parado at irse_derecha_caminando
    hide jugador argentina
    hide ju polonia with dissolve
    "El partido continuó muy cerrado hasta el comienzo del segundo tiempo."
    "Minuto 46."
    "Nahuel Molina avanzó audazmente por el lateral derecho, esquivando a varios defensores polacos con velocidad y precisión."

    scene Comentarista
    Paoli "¡Atención con Molina, que se mete por la derecha! ¡Puede ser peligrosa!"

    $ Molina = Character("Nahuel Molina", color="#74b9ff")
    Molina "¡Entrá al área, Alexis!"

    scene Cancha esquina:
        zoom 1.3
    show jugador argentina at focus:
        xalign -0.2 yalign 1.0
        easein 0.4 xalign 0.4
    show ju polonia at dim:
        xalign 0.8 yalign 1.0
    "Molina levantó la cabeza y lanzó un centro preciso hacia el área. Allí apareció Alexis Mac Allister, quien llegó desde atrás y conectó un potente remate imposible de detener."

    scene Estadio at terremoto
    play sound "Aficion_EX.ogg" volume 0.3
    Aficion "¡¡¡GOOOOOOOOOOOL!!!"

    scene Comentarista
    Paoli "¡Gol de Argentina! ¡Gol de Mac Allister! ¡La selección rompe el empate apenas comienza el segundo tiempo y ahora está más cerca de los octavos de final!"

    $ MacAllister = Character("Alexis Mac Allister", color="#74b9ff")
    MacAllister "¡Vamos! ¡No aflojemos ahora!"

    scene Cancha esquina with dissolve
    hide jugador argentina
    hide ju polonia
    "Después de ampliar la ventaja, la siguiente oportunidad de gol llegó solo unos minutos más tarde."
    "Minuto 67."
    "Julián Álvarez recibió el balón cerca del área y comenzó a avanzar rápidamente entre los defensores polacos. Con gran velocidad logró superar la marca de varios jugadores y quedó frente al arco."

    scene Comentarista
    Paoli "¡Atención con Julián! ¡Se mete al área, puede ser el segundo!"

    $ Julian = Character("Julián Álvarez", color="#74b9ff")
    Julian "¡Esta entra sí o sí!"

    scene Estadio at terremoto with flash_wakeup
    play sound "Aficion_EX.ogg" volume 0.3
    Aficion "¡¡¡GOOOOOOOOOOOL!!!"

    scene Comentarista
    Paoli "¡Golazo de Julián Álvarez! ¡Argentina amplía la diferencia y ahora gana 2-0 frente a Polonia!"

    scene Cancha esquina with dissolve
    show jugador argentina at dim:
        xalign 0.6 yalign 1.0
    show Messi parado at focus:
        entrar_izquierda
    "El diez abrazó a Julián mientras sonreía."

    M "¡Bien, Julián! ¡Así se juega!"

    show Messi parado at dim
    "Tras el segundo gol, el partido comenzó a quedarse estancado. Argentina manejaba la posesión con tranquilidad mientras Polonia intentaba reaccionar, pero la defensa argentina se mantenía firme y no deja espacios."
    "La selección polaca no pudo hacer mucho más que seguir luchando y dar lo mejor de sí hasta el final del encuentro."
    
    scene Estadio with flash_wakeup
    "Finalmente, el árbitro hizo sonar el silbato."
    "*(Piiiiiiiiiiip)*"

    scene Comentarista
    Paoli "¡Final del partido! ¡Argentina gana 2-0 contra Polonia y clasifica a los octavos de final del mundial como líder de grupo!"

    stop music fadeout 2.0
    stop sound fadeout 2.0

    return




    
    
