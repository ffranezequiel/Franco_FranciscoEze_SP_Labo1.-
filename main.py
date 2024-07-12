import pygame 
from constantes import *
from data import lista
import json
from funciones import *


pregunta = ""
texto_pregunta = []
texto_respuesta_a = []
texto_respuesta_b = []
texto_respuesta_c = []
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
respuesta_correcta = ""
respuesta_elegida = ""
lista_preguntas = []
lista_respuesta_a = []
lista_respuesta_b = []
lista_respuesta_c = []
lista_respuesta_correcta = []
tiempo = 0
posicion = 0
puntaje = 0
ingresando_nombre = ""

for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])
    lista_respuesta_a.append(e_lista["a"])
    lista_respuesta_b.append(e_lista["b"])
    lista_respuesta_c.append(e_lista["c"])
    lista_respuesta_correcta.append(e_lista["correcta"])


pygame.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Carrera UTN")

#--------FUENTES-----
fuente = pygame.font.SysFont("Impact", 30,False,True)
fuente_mini = pygame.font.SysFont("Impact", 35,False,True)
fuente_dos = pygame.font.SysFont("Arial", 18)
fuente_tres = pygame.font.SysFont("Impact", 12,False,True)
fuente_pregunta = pygame.font.SysFont("Impact",20)

#-----TEXTOS--
# texto_pregunta = fuente_dos.render(str(pregunta), True, COLOR_NEGRO)
texto_respuesta_a_ = fuente_dos.render(str(respuesta_a), True, COLOR_BLANCO)
texto_respuesta_b_ = fuente_dos.render(str(respuesta_b), True, COLOR_BLANCO)
texto_respuesta_c_ = fuente_dos.render(str(respuesta_c), True, COLOR_BLANCO)
texto_tiempo = fuente.render(str("Tiempo: "), True, COLOR_BLANCO)
texto_puntaje_txt = fuente.render(str("Puntaje: "), True, COLOR_BLANCO)
texto_puntaje = fuente.render(str("0"), True, COLOR_BLANCO)

texto_avanza_uno = fuente_tres.render(str("Avanza 1"), True, COLOR_NEGRO)
texto_retrocede_uno = fuente_tres.render(str("Retrocede 1"), True, COLOR_NEGRO)
texto_vuelve_inicio = fuente_tres.render(str("Vuelve al"), True, COLOR_NEGRO)
texto_vuelve_inicio_2 = fuente_tres.render(str("inicio"), True, COLOR_NEGRO)

#-------IMAGENES-------
fondo = pygame.image.load("imagenes\sand_brick.png") 
fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))
imagen_principal = pygame.image.load("imagenes\portada.png")
imagen_principal = pygame.transform.scale(imagen_principal, (240, 220))

img_star = pygame.image.load("imagenes\start_btn.png")
img_star= pygame.transform.scale(img_star,(130,70))
img_exit = pygame.image.load("imagenes\exit_btn.png")
img_exit = pygame.transform.scale(img_exit,(130,70))

imagen_personaje = pygame.image.load("imagenes\personaje.png")
imagen_personaje = pygame.transform.scale(imagen_personaje, (55, 120))

imagen_utn = pygame.image.load("imagenes\dfile.png")
imagen_utn = pygame.transform.scale(imagen_utn, (130, 80))
imagen_flecha = pygame.image.load("imagenes\dflecha.png")
imagen_flecha = pygame.transform.scale(imagen_flecha, (130, 80))

#---TIMER-----
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000) # 1000 es un segundo
segundos = "5"
timer_total = TIEMPO_MAXIMO_SEGUNDOS 

#----SONIDOS----
pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("sonidos\music.wav")
sonido_lost = pygame.mixer.Sound("sonidos\BD19.WAV")
sonido_avanza = pygame.mixer.Sound("sonidos\SONIC.wav")
sonido_correcto = pygame.mixer.Sound("sonidos\q7607.mp3")
sonido_error = pygame.mixer.Sound("sonidos\error.mp3")
sonido_vuelve_principio = pygame.mixer.Sound("sonidos\cuak.mp3")
volumen = 0.12
sonido_fondo.set_volume(volumen)

#---RECTANGULOS--
rect_btn_star = pygame.Rect(255, 495, 130, 70)
rect_btn_exit = pygame.Rect(500, 500, 130, 70)
rect_utn = pygame.Rect(100, 200, 150, 40)
rect_logo = pygame.Rect(200, 400, 150, 40)
rect_personaje = pygame.Rect(120, 240, 150, 40)
rect_opcion_a =pygame.Rect(245,110,120,120)
rect_opcion_b =pygame.Rect(370,110,120,120)
rect_opcion_c = pygame.Rect(500,110,120,120)
rect_finish = pygame.Rect(55, 375, 150, 40)

#---BANDERAS---
flag_run = True
tiempo_iniciado = False
fin_tiempo = False


while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = list(evento.pos)
            print(click)
            #COLLIDEPOINT ENTRE EL CLICK Y BOTON START
            if rect_btn_star.collidepoint(click):
                pregunta = lista_preguntas[posicion]
                respuesta_a = lista_respuesta_a[posicion]
                respuesta_b = lista_respuesta_b[posicion]
                respuesta_c = lista_respuesta_c[posicion]
                respuesta_correcta = lista_respuesta_correcta[posicion]
                texto_pregunta = render_texto(pregunta, fuente_pregunta, COLOR_BLANCO, 350)
                texto_respuesta_a = render_texto(respuesta_a, fuente_pregunta, COLOR_BLANCO, 100)
                texto_respuesta_b = render_texto(respuesta_b, fuente_pregunta, COLOR_BLANCO, 100)
                texto_respuesta_c = render_texto(respuesta_c, fuente_pregunta, COLOR_BLANCO, 100)
                tiempo_iniciado = True
                segundos = 5
                timer_total = TIEMPO_MAXIMO_SEGUNDOS 
            #COLLIDEPOINT ENTRE EL CLICK Y BOTON EXIT
            elif rect_btn_exit.collidepoint(click):
                ingresando_nombre = pedir_nombre(pantalla, fuente)
                if ingresando_nombre:
                    guardar_puntaje(ingresando_nombre, puntaje)
                    mostrar_mejores_puntajes(pantalla, fuente)
                pregunta = ""
                respuesta_a = ""
                respuesta_b = ""
                respuesta_c = ""
                texto_pregunta = []
                texto_respuesta_a = []
                texto_respuesta_b = []
                texto_respuesta_c = []
                puntaje = 0
                posicion = 0
                segundos = 5
                rect_personaje = pygame.Rect(120, 240, 150, 40)
                tiempo_iniciado = False
                timer_total = TIEMPO_MAXIMO_SEGUNDOS 
            
            #COLISION CUANDO EL PERSONAJE CHOCA CON LA META FINAL
            elif rect_personaje.colliderect(rect_finish):
                ingresando_nombre = pedir_nombre(pantalla, fuente)
                if ingresando_nombre:
                    guardar_puntaje(ingresando_nombre, puntaje)
                    mostrar_mejores_puntajes(pantalla, fuente)
                pregunta = ""
                respuesta_a = ""
                respuesta_b = ""
                respuesta_c = ""
                texto_pregunta = []
                texto_respuesta_a = []
                texto_respuesta_b = []
                texto_respuesta_c = []
                puntaje = 0
                posicion = 0
                segundos = 5
                rect_personaje = pygame.Rect(120, 240, 150, 40)
                tiempo_iniciado = False
                timer_total = TIEMPO_MAXIMO_SEGUNDOS 

            #--------ELECCION DE RESPUESTAS----
            if tiempo_iniciado:  
                if rect_opcion_a.collidepoint(click):
                    respuesta_elegida = "a"
                elif rect_opcion_b.collidepoint(click):
                    respuesta_elegida = "b"
                elif rect_opcion_c.collidepoint(click):
                    respuesta_elegida = "c"
                else:
                    respuesta_elegida = None
                #--------MOVIMIENTO DEL PERSONAJE POR CORDENADAS----
                if respuesta_elegida == respuesta_correcta:
                    sonido_correcto.play()
                    puntaje += 10
                    if rect_personaje.x < 570 and rect_personaje.y < 375: #mover de a dos casilleros 
                        rect_personaje.move_ip(130, 0)
                    elif rect_personaje.x > 570 and rect_personaje.x < 630 and rect_personaje.y < 375: #saltar a la fila de abajo
                        rect_personaje.x = 640
                        rect_personaje.y = 375
                    elif rect_personaje.x > 630 and rect_personaje.y < 375:  #saltar a la fila de abajo
                        rect_personaje.x = 570
                        rect_personaje.y = 375
                    elif rect_personaje.x > 70 and rect_personaje.y > 370: #avanzar en fila de abajo
                        rect_personaje.move_ip(-130, 0)
                    elif rect_personaje.x < 300 and rect_personaje.y > 375: 
                        if respuesta_elegida == respuesta_correcta:
                            rect_personaje.x = 70
                            rect_personaje.y = 375
                            ingresando_nombre = pedir_nombre(pantalla, fuente)
                            if ingresando_nombre:
                                guardar_puntaje(ingresando_nombre, puntaje)
                                mostrar_mejores_puntajes(pantalla, fuente)
                
                elif respuesta_elegida is not respuesta_correcta and respuesta_elegida is not None:
                    sonido_error.play()
                    if rect_personaje.x == 120 and rect_personaje.y == 240:
                        rect_personaje.x = 120
                        rect_personaje.y = 240
                    elif rect_personaje.x < 700 and rect_personaje.y < 375:
                        rect_personaje.move_ip(-65, 0)
                    elif rect_personaje.x > 630 and rect_personaje.y > 350:
                        rect_personaje.x = 635
                        rect_personaje.y = 250
                    elif rect_personaje.x > 70 and rect_personaje.y > 370:
                        rect_personaje.move_ip(65, 0)
                        
                
                #----ACTUALIZACION DEL PUNTAJE
                texto_puntaje = fuente.render(str(puntaje), True, COLOR_BLANCO)
                #---VERIFICACION SI SE PASARON TODAS LAS PREGUNTAS---
                if posicion < len(lista_preguntas):
                    pregunta = lista_preguntas[posicion]
                    respuesta_a = lista_respuesta_a[posicion]
                    respuesta_b = lista_respuesta_b[posicion]
                    respuesta_c = lista_respuesta_c[posicion]
                    respuesta_correcta = lista_respuesta_correcta[posicion]
                    texto_pregunta = render_texto(pregunta, fuente_pregunta, COLOR_BLANCO, 350)
                    texto_respuesta_a = render_texto(respuesta_a, fuente_pregunta, COLOR_BLANCO, 100)
                    texto_respuesta_b = render_texto(respuesta_b, fuente_pregunta, COLOR_BLANCO, 100)
                    texto_respuesta_c = render_texto(respuesta_c, fuente_pregunta, COLOR_BLANCO, 100)
                    segundos = 5  
                else:
                    fin_tiempo = True
                posicion += 1
        #-----------------TIMER 5 SEGUNDOS PREGUNTAS----------
        if evento.type == timer_segundos and tiempo_iniciado:
            if not fin_tiempo:
                segundos -= 1
                if segundos == -1:
                    posicion += 1
                    if posicion < len(lista_preguntas)-1:
                        
                        pregunta = lista_preguntas[posicion]
                        respuesta_a = lista_respuesta_a[posicion]
                        respuesta_b = lista_respuesta_b[posicion]
                        respuesta_c = lista_respuesta_c[posicion]
                        respuesta_correcta = lista_respuesta_correcta[posicion]
                        texto_pregunta = render_texto(pregunta, fuente_pregunta, COLOR_BLANCO, 350)
                        texto_respuesta_a = render_texto(respuesta_a, fuente_pregunta, COLOR_BLANCO, 100)
                        texto_respuesta_b = render_texto(respuesta_b, fuente_pregunta, COLOR_BLANCO, 100)
                        texto_respuesta_c = render_texto(respuesta_c, fuente_pregunta, COLOR_BLANCO, 100)
                        segundos = 5 
                    else:
                        fin_tiempo = True
                        ingresando_nombre = pedir_nombre(pantalla, fuente)
                        if ingresando_nombre:
                            guardar_puntaje(ingresando_nombre, puntaje)
                            mostrar_mejores_puntajes(pantalla, fuente)
        
        #-----------------TIMER RELOJ TOTAL----------
        if evento.type == timer_segundos and tiempo_iniciado:
            timer_total -= 1
            if timer_total <= 0:
                if not fin_tiempo:
                    fin_tiempo = True
                    ingresando_nombre = pedir_nombre(pantalla, fuente)
                    if ingresando_nombre:
                        guardar_puntaje(ingresando_nombre, puntaje)
                        mostrar_mejores_puntajes(pantalla, fuente)
                    posicion = 0
                    puntaje = 0
                    tiempo_iniciado = False
                    segundos = 5
                    timer_total = TIEMPO_MAXIMO_SEGUNDOS 
                    pregunta = ""
                    respuesta_a = ""
                    respuesta_b = ""
                    respuesta_c = ""
                    texto_pregunta = []
                    texto_respuesta_a = []
                    texto_respuesta_b = []
                    texto_respuesta_c = []
                    rect_personaje = pygame.Rect(120, 240, 150, 40)
            
        
    #CASILLEROS DE AVANZA 1, RETROCEDE 1 O VUELVE AL PRINCIPIO
    if rect_personaje.x > 505 and rect_personaje.x < 560 and rect_personaje.y < 340:
        sonido_avanza.play()
        rect_personaje.move_ip(65, 0)
    elif rect_personaje.x > 375 and rect_personaje.x < 435 and rect_personaje.y > 340:
        sonido_lost.play()
        rect_personaje.move_ip(65, 0)
    elif rect_personaje.x > 630 and rect_personaje.x < 690 and rect_personaje.y < 340:
        sonido_vuelve_principio.play()
        rect_personaje.x = 120  # Vuelve a la posicion inicial del juego
        rect_personaje.y = 240  
        puntaje = 0
        texto_puntaje = fuente.render(str(puntaje), True, COLOR_BLANCO)
    
    #-------PANTALLA----
    pantalla.blit(fondo,(0,0))
    #------FUNCION QUE DIBUJA LOS ESCALONES---
    dibujar_rects_escalones(pantalla)
    #----BLITEO DE SEGUNDOS---
    segundos_finales = fuente.render(str(f"Reloj: {timer_total}"),True,COLOR_BLANCO)
    pantalla.blit(segundos_finales,(15,220))
    segundos_texto = fuente.render(str(segundos), True, COLOR_BLANCO)
    pantalla.blit(segundos_texto, (720, 35))
    
    #---IMAGENES----
    pantalla.blit(imagen_principal, (0, 0))
    pantalla.blit(imagen_utn, (40, 400))
    pantalla.blit(imagen_personaje, (rect_personaje.x, rect_personaje.y))
    pantalla.blit(imagen_flecha,(660,340))
    pantalla.blit(img_star,(200,520))
    pantalla.blit(img_exit,(490,520))
    
    #---TEXTOS EN PANTALLA--
    pantalla.blit(texto_tiempo, (610, 35))
    pantalla.blit(texto_puntaje_txt, (610, 100))
    pantalla.blit(texto_puntaje, (720, 100))
    #----FUNCION QUE MUESTRA LAS PREGUNTAS CON SUS RESPECTIVAS OPCIONES
    dibujar_textos(pantalla,texto_pregunta,texto_respuesta_a,texto_respuesta_b,texto_respuesta_c)
    pantalla.blit(texto_avanza_uno, (513, 303))
    pantalla.blit(texto_retrocede_uno, (376, 425))
    pantalla.blit(texto_vuelve_inicio, (640, 295))
    pantalla.blit(texto_vuelve_inicio_2, (650, 310))

    pygame.display.flip()
pygame.quit()