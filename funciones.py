import pygame
from constantes import *
import json

#FUNCION PARA GUARDAR PUNTAJE
def guardar_puntaje(nombre, puntaje):
    try:
        with open('puntajes.json', 'r') as archivo:
            puntajes = json.load(archivo)
    except FileNotFoundError:
        puntajes = []

    puntajes.append({'nombre': nombre, 'puntaje': puntaje})
    puntajes = sorted(puntajes, key=lambda x: x['puntaje'], reverse=True)[:10]

    with open('puntajes.json', 'w') as archivo:
        json.dump(puntajes, archivo, indent=4)

# Función para mostrar los mejores puntajes
def mostrar_mejores_puntajes():
    try:
        with open('puntajes.json', 'r') as archivo:
            puntajes = json.load(archivo)
    except FileNotFoundError:
        puntajes = []

    print("Top 10 Puntajes:")
    for i, puntaje in enumerate(puntajes):
        print(f"{i+1}. {puntaje['nombre']} - {puntaje['puntaje']} puntos")

fondo = pygame.image.load("imagenes\sand_brick.png") 
fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

#FUNCION PARA MOSTRAR PUNTUACIONES
def mostrar_puntuaciones(pantalla, puntajes):
    pantalla.blit(fondo, (0,0))
    fuente = pygame.font.SysFont("Impact", 35)
    texto = fuente.render("Mejores Puntajes: ", True, COLOR_BLANCO)
    pantalla.blit(texto, (300, 50))

    y = 100  # Posición inicial en y para los puntajes
    for i, j in enumerate(puntajes):
        texto = f"{i + 1}. {j['nombre']} - {j['puntaje']} puntos"
        render = fuente.render(texto, True, COLOR_BLANCO)
        pantalla.blit(render, (300, y))
        y += 50  # Incrementa la posición para el siguiente puntaje
    pygame.display.flip()
    pygame.time.wait(4000) #espera 5 segundos y cierra


