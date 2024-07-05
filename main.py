import pygame
from constantes import *
from data import lista
from funciones import guardar_puntaje,mostrar_mejores_puntajes,mostrar_puntuaciones
import json

#Recorrer la lista guardando en sub-listas: la pregunta, cada opción, el tema y la respuesta correcta.
lista_preguntas = []
lista_opcion_a = []
lista_opcion_b = []
lista_opcion_c = []
lista_tema = []
lista_respuestas_correcta = []

for i in lista:
    lista_preguntas.append(i['pregunta'])
    lista_opcion_a.append(i['a'])
    lista_opcion_b.append(i['b'])
    lista_opcion_c.append(i['c'])
    lista_respuestas_correcta.append(i['correcta'])
    lista_tema.append(i['tema'])

#INICIALIZACION DE VARIABLES
preguntas = ""
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
posicion = 0
puntaje = 0
errores = 0
respuesta_correcta = False
segundos = "5"
fin_tiempo = False
pos_img = [0,0]
pos_x, pos_y = 0, 0
casillas_avanza_1 = [6]  
casillas_retrocede_2 = [12]

#----------------- INICIO PYGAME ------------------
pygame.init()

#-------TIMER------
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000)
#------SONIDOS------
pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("sonidos\music.wav")
sonido_lost = pygame.mixer.Sound("sonidos\BD19.WAV")
sonido_avanza = pygame.mixer.Sound("sonidos\SONIC.wav")
volumen = 0.12
sonido_fondo.set_volume(volumen)

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Carrera UTN")

#--------IMAGENES----
fondo = pygame.image.load("imagenes\sand_brick.png") 
fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))
imagen = pygame.image.load("imagenes\portada.png")
imagen= pygame.transform.scale(imagen,(280,200))

imagen_utn = pygame.image.load("imagenes\dfile.png")
imagen_utn = pygame.transform.scale(imagen_utn,(90,70))
rect_utn = pygame.Rect(120,400,175,350)
imagen_personaje = pygame.image.load("imagenes\personaje.png")
imagen_personaje = pygame.transform.scale(imagen_personaje,(90,90))
rect_personaje = pygame.Rect(120,260,175,350)

imagen_flecha = pygame.image.load("imagenes\dflecha.png")
imagen_flecha = pygame.transform.scale(imagen_flecha,(70,55))
img_star = pygame.image.load("imagenes\start_btn.png")
img_star= pygame.transform.scale(img_star,(130,70))
img_exit = pygame.image.load("imagenes\exit_btn.png")
img_exit = pygame.transform.scale(img_exit,(130,70))

#-------TIPOS DE FUENTE--------
fuente =  pygame.font.SysFont("Impact", 20)
fuente_dos =  pygame.font.SysFont("Impact", 15)
fuente_mini =  pygame.font.SysFont("Impact", 35,False,True)
fuente_preguntas = pygame.font.SysFont("Arial", 30, True, True)

texto_tiempo_txt = fuente_mini.render("TIEMPO: ", True, COLOR_BLANCO)
texto_puntaje_txt = fuente_mini.render("PUNTAJE: ", True,COLOR_BLANCO)

texto_pregunta = fuente_mini.render(str(preguntas),True,COLOR_BLANCO )
texto_respuesta_a = fuente.render(str(respuesta_a), True,COLOR_NEGRO)
texto_respuesta_b = fuente.render(str(respuesta_b), True,COLOR_NEGRO)
texto_respuesta_c = fuente.render(str(respuesta_c), True,COLOR_NEGRO)
texto_puntaje = fuente_mini.render(str(puntaje),True,COLOR_BLANCO )
texto_avanza_dos = fuente_dos.render(str("AVANZA 1"), True, COLOR_BLANCO)
texto_retrocede_uno = fuente_dos.render(str("RETROCEDE 1"), True, COLOR_BLANCO)

posiciones_tablero = [(140,280), # Posición inicial (partida) 
    (205, 280),  
    (285, 280),
    (365, 280),
    (445, 280),
    (525, 280),
    (605, 280),
    (685, 280),
    (765, 280),
    (765, 400),
    (685, 400),
    (605, 400),
    (525, 400),
    (445, 400),
    (365, 400),
    (285, 400),
    (205, 400),
    (250, 400)   # Posición final (meta)
]

flag_correr = True
flag_btn_star = False
flag_btn_exit = False
ingresando_nombre = False
nombre_jugador = ""

while flag_correr:
    
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = list(evento.pos)
            print(click)
    
    #---------------------------------MENU PRINCIPAL------------------------------------
            if (click[0] > 255 and click[0] < 390 ) and (click[1] > 495 and click[1] < 570):
        
                sonido_fondo.play()
                flag_btn_star = True    
                errores = 0
                respuesta_correcta = False
                ingresando_nombre = False
                puntaje = 0
                posicion = 0
                segundos = 5
    #--------------------------------REINICIAR/TERMINAR------------------------ 
            if (click[0]>500 and click[0]<635) and (click[1]>500 and click[1]<570):
                flag_btn_exit = True
                flag_btn_star = False
                puntajes = json.load(open('puntajes.json', 'r'))
                mostrar_puntuaciones(pantalla, puntajes)
               
            if posicion < len(lista_preguntas):
        #------------------------------Respuesta A--------------------------------- 
                if (click[0]> 240 and click[0] < 480) and (click[1] > 80 and click[1] < 200):
                    if lista_respuestas_correcta[posicion] == "a":
                        respuesta_correcta = True
                    else:
                        errores += 1
        
        #------------------------------Respuesta B--------------------------------
                if (click[0]>480 and click[0]<700) and (click[1]>80 and click[1]<200):   
                    if lista_respuestas_correcta[posicion] == "b":
                        respuesta_correcta = True
                    else:
                        errores = errores + 1 

        ##------------------------------Respuesta C--------------------------------
                if (click[0] > 700 and click[0] < 940) and (click[1]>80 and click[1]<200):                   
                    if  lista_respuestas_correcta[posicion] == "c":
                        respuesta_correcta = True
                    else:
                        errores = errores + 1 
                
                
                #-----------MOVER PERSONAJE--------
                if respuesta_correcta:
                    puntaje += 10
                    texto_puntaje = fuente_mini.render(str(puntaje), True, COLOR_BLANCO)
                    if posicion + 1 < len(posiciones_tablero):
                        posicion += 2
                    else:
                        posicion = len(posiciones_tablero) - 1

                    if posicion in casillas_avanza_1:
                        sonido_avanza.play()
                        if posicion + 1 < len(posiciones_tablero):
                            posicion += 1
                    elif posicion in casillas_retrocede_2:
                        sonido_lost.play()
                        if posicion - 2 >= 0:
                            posicion -= 1

                    pos_x, pos_y = posiciones_tablero[posicion]
                    respuesta_correcta = False
                    segundos = 5

                if errores > 0:
                    if posicion - 1 >= 0:
                        posicion -= 1
                    # else:
                    #     posicion = 0
                    pos_x, pos_y = posiciones_tablero[posicion]
                    errores = 0
                    segundos = 5

                    #------MANEJO TIEMPO---------

        if evento.type == pygame.USEREVENT and flag_btn_star == True:
            segundos = int (segundos) -1
            if int(segundos) == -1:
                # if respuesta_correcta:
                if posicion + 1 <len(lista_preguntas):
                    posicion +=1
                else:
                    posicion = len(lista_preguntas) - 1
                segundos = 5  # Reiniciar el tiempo
                pos_x, pos_y = posiciones_tablero[posicion]
                respuesta_correcta = False 

        if evento.type == pygame.KEYDOWN and ingresando_nombre:
            if evento.key == pygame.K_RETURN:
                guardar_puntaje(nombre_jugador, puntaje)
                mostrar_mejores_puntajes()
                ingresando_nombre = False
                flag_btn_exit = False
                nombre_jugador = ""
            else:
                nombre_jugador += evento.unicode

    if flag_btn_exit and not ingresando_nombre:
        puntajes = json.load(open('puntajes.json', 'r'))
        mostrar_puntuaciones(pantalla, puntajes)
        ingresando_nombre= True
                
    #------------------PANTALLA------------------------
    pantalla.blit(fondo, (0,0))
    pantalla.blit(imagen_personaje, posiciones_tablero[posicion])
    # pantalla.blit(imagen_utn, posiciones_tablero[-1])
    
    if flag_btn_star:
        if posicion < len(lista_preguntas):
            pregunta = lista_preguntas[posicion]
            respuesta_a = lista_opcion_a[posicion]
            respuesta_b =  lista_opcion_b[posicion]
            respuesta_c = lista_opcion_c[posicion]

            texto_pregunta = fuente.render(str(pregunta), True, COLOR_BLANCO)
            texto_respuesta_a = fuente.render(str(respuesta_a), True,COLOR_BLANCO)
            texto_respuesta_b = fuente.render(str(respuesta_b), True,COLOR_BLANCO)
            texto_respuesta_c = fuente.render(str(respuesta_c), True,COLOR_BLANCO)
            segundos_tiempo = fuente_mini.render(str(segundos),True, COLOR_BLANCO)

            # pantalla.blit(imagen_personaje,rect_personaje)
            pantalla.blit(imagen_utn,rect_utn)
            pantalla.blit(texto_tiempo_txt,(750, 470))
            pantalla.blit(texto_puntaje_txt,(750, 530))
            pantalla.blit(segundos_tiempo,(880,470))
            pantalla.blit(texto_pregunta,(450,50))
            pantalla.blit(texto_respuesta_a,(340,143))
            pantalla.blit(texto_respuesta_b,(540,143))
            pantalla.blit(texto_respuesta_c,(760,143)) 
            pantalla.blit(texto_puntaje,(880,530))
            pantalla.blit(imagen_flecha,(776, 346))
            pantalla.blit(texto_avanza_dos,(620,315))
            pantalla.blit(texto_retrocede_uno,(540,415))
            pantalla.blit(imagen_personaje, (pos_x, pos_y))

             #ESCALONES HACIA LA META
            pygame.draw.ellipse(pantalla, LIGHT_BLUE,(220,300,60,50),1)
            pygame.draw.ellipse(pantalla, PURPLE,(300,300,60,50),1)
            pygame.draw.ellipse(pantalla, PINK,(380,300,60,50),1)
            pygame.draw.ellipse(pantalla, TURQUESA,(460,300,60,50),1)
            pygame.draw.ellipse(pantalla, YELLOW_GREEN,(540,300,60,50),1)
            pygame.draw.ellipse(pantalla, NAVY,(620,300,60,50),1)
            pygame.draw.ellipse(pantalla, DARK_RED,(700,300,60,50),1)
            pygame.draw.ellipse(pantalla, CYAN,(780,300,60,50),1)

            pygame.draw.ellipse(pantalla, CYAN,(780,400,60,50),1)
            pygame.draw.ellipse(pantalla, DARK_RED,(700,400,60,50),1)
            pygame.draw.ellipse(pantalla, NAVY,(620,400,60,50),1)
            pygame.draw.ellipse(pantalla, YELLOW_GREEN,(540,400,60,50),1)
            pygame.draw.ellipse(pantalla, TURQUESA,(460,400,60,50),1)
            pygame.draw.ellipse(pantalla, PINK,(380,400,60,50),1)
            pygame.draw.ellipse(pantalla, PURPLE,(300,400,60,50),1)
            pygame.draw.ellipse(pantalla, LIGHT_BLUE,(220,400,60,50),1)
        else:
            texto_fin = fuente.render("JUEGO TERMINADO!", True, COLOR_BLANCO)
            texto_puntaje_final = fuente.render(f"PUNTAJE FINAL: {puntaje}", True, COLOR_BLANCO)
            pantalla.blit(texto_fin, (370,200))
            pantalla.blit(texto_puntaje_final, (400,240))
            ingresando_nombre = True
            flag_btn_star = False
            segundos = 5 

    elif ingresando_nombre:
        pantalla.blit(fondo, (0,0))
        pantalla.blit(imagen_personaje, posiciones_tablero[posicion])
        texto = fuente_mini.render(f"Nombre: {nombre_jugador}", True, COLOR_BLANCO)
        pantalla.blit(texto, (220, 300))
    else:
        pantalla.blit(imagen,(pos_img))
        pantalla.blit(img_exit, (500,500)) 
        pantalla.blit(img_star, (260,500))
        
    pantalla.blit(imagen,(pos_img))
    pantalla.blit(img_star,(260,500))
    pantalla.blit(img_exit,(500,500))
    
    pygame.display.flip()
pygame.quit()