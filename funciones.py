import pygame
from constantes import *
import json

fondo = pygame.image.load("imagenes\sand_brick.png") 
fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))
imagen_principal = pygame.image.load("imagenes\portada.png")
imagen_principal = pygame.transform.scale(imagen_principal, (240, 220))
imagen_personaje = pygame.image.load("imagenes\personaje.png")
imagen_personaje = pygame.transform.scale(imagen_personaje, (200, 220))

def render_texto(texto, fuente, color, max_ancho):
    palabras = texto.split(' ')
    lineas = []
    linea_actual = palabras[0]
    for palabra in palabras[1:]:
        if fuente.size(linea_actual + ' ' + palabra)[0] <= max_ancho:
            linea_actual += ' ' + palabra
        else:
            lineas.append(linea_actual)
            linea_actual = palabra
    lineas.append(linea_actual)
    return [fuente.render(linea, True, color) for linea in lineas]


def pedir_nombre(pantalla, fuente):
    nombre = ""
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return None
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return nombre
                else:
                    nombre += evento.unicode
        pantalla.blit(fondo,(0,0))
        pantalla.blit(imagen_principal,(0,0))
        texto = fuente.render("Ingresa tu nombre: " + nombre, True, COLOR_BLANCO)
        pantalla.blit(texto, (200, 250))
        pygame.display.flip()



def guardar_puntaje(nombre, puntaje):
    archivo_puntajes = "puntajes.json"
    try:
        with open(archivo_puntajes, "r") as archivo:
            puntajes = json.load(archivo)
    except FileNotFoundError:
        puntajes = []
    puntajes.append({"nombre": nombre, "puntaje": puntaje})
    puntajes = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)[:10]
    with open(archivo_puntajes, "w") as archivo:
        json.dump(puntajes, archivo)


def mostrar_mejores_puntajes(pantalla, fuente):
    archivo_puntajes = "puntajes.json"
    try:
        with open(archivo_puntajes, "r") as archivo:
            puntajes = json.load(archivo)
    except FileNotFoundError:
        puntajes = []
    pantalla.blit(fondo,(0,0))
    pantalla.blit(imagen_principal,(0,0))
    pantalla.blit(imagen_personaje,(50,280))
    titulo = fuente.render("Mejores Puntajes", True, COLOR_BLANCO)
    pantalla.blit(titulo, (300, 40))
    posicion_y = 80
    for i, puntaje in enumerate(puntajes):
        texto = fuente.render(f"{i + 1} {puntaje['nombre'].capitalize()} - {puntaje['puntaje']}", True, COLOR_BLANCO)
        pantalla.blit(texto, (300, posicion_y))
        posicion_y += 50
    pygame.display.flip()
    pygame.time.wait(6000)

def dibujar_textos(pantalla, texto_pregunta, texto_respuesta_a, texto_respuesta_b, texto_respuesta_c):
    for i, linea in enumerate(texto_pregunta):
        pantalla.blit(linea, (245, 30 + i * 30))
    for i, linea in enumerate(texto_respuesta_a):
        pantalla.blit(linea, (245, 150 + i * 30))
    for i, linea in enumerate(texto_respuesta_b):
        pantalla.blit(linea, (375, 150 + i * 30))
    for i, linea in enumerate(texto_respuesta_c):
        pantalla.blit(linea, (500, 150 + i * 30))

def dibujar_rects_escalones(pantalla):
    for i, color in enumerate(LISTA_COLORES):
        pygame.draw.rect(pantalla, color, (180 + 65 * i, 280, 60, 60), border_radius=15)
        pygame.draw.rect(pantalla, color, (180 + 65 * i, 400, 60, 60), border_radius=15)


