import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Lab 2 Zad. 1")

PROMIEN = 150
SRODEK = (300, 300)
ILOSC_WIERZCHOLKOW = 8

punkty = []
for i in range(ILOSC_WIERZCHOLKOW):
    kat = (2 * math.pi / ILOSC_WIERZCHOLKOW) * i
    x = PROMIEN * math.cos(kat)
    y = PROMIEN * math.sin(kat)
    punkty.append((x, y))

KOLOR = (120, 26, 180)  # Fioletowy

SCALE = (1, 1)  # skalowanie obrazu (szerokość, wysokość)
ROTATION = 0  # obracanie obrazu (stopnie w prawo)
SHEAR = 0  # przekształcenie nożycowe
TRANSLATE = (0, 0)  # przesunięcie (x, y)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                SCALE = (1, 1)
                ROTATION = 0
                SHEAR = 0
                TRANSLATE = (0, 0)
            elif event.key == pygame.K_1:
                SCALE = (0.2, 0.2)
            elif event.key == pygame.K_2:
                ROTATION = 20
            elif event.key == pygame.K_3:
                SCALE = (-0.2, -0.6)
            elif event.key == pygame.K_4:
                SHEAR = 0.5
            elif event.key == pygame.K_5:
                TRANSLATE = (0, -200)
                SCALE = (1, 0.5)
            elif event.key == pygame.K_6:
                SCALE = (1.5, 1.5)
                ROTATION = 90
                SHEAR = 0.5
            elif event.key == pygame.K_7:
                SCALE = (0.2, -0.6)
            elif event.key == pygame.K_8:
                TRANSLATE = (-80, 80)
                SCALE = (1, 0.5)
                ROTATION = 20
            elif event.key == pygame.K_9:
                TRANSLATE = (120, 0)
                ROTATION = 180
                SHEAR = 0.5

    win.fill((255,255,255))  # Czyszczenie ekranu

    # Rysowanie przekształconych punktów
    przeksztalcone_punkty = []
    for (x, y) in punkty:
        # Przeniesienie środka figury do (0,0)
        x -= 0
        y -= 0

        # Przekształcenie nożycowe
        x_shear = x + SHEAR * y
        y_shear = y

        # Skalowanie
        x_scale = x_shear * SCALE[0]
        y_scale = y_shear * SCALE[1]

        # Rotacja
        kat_rad = math.radians(ROTATION)
        x_rot = x_scale * math.cos(kat_rad) - y_scale * math.sin(kat_rad)
        y_rot = x_scale * math.sin(kat_rad) + y_scale * math.cos(kat_rad)

        # Przywrócenie środka i przesunięcie figury
        x_final = x_rot + SRODEK[0] + TRANSLATE[0]
        y_final = y_rot + SRODEK[1] + TRANSLATE[1]

        przeksztalcone_punkty.append((x_final, y_final))

    pygame.draw.polygon(win, KOLOR, przeksztalcone_punkty)

    pygame.display.update()

pygame.quit()
