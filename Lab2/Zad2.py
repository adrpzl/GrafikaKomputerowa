import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Lab 2 Zad. 2")

KOLOR = (255, 0, 0)

srodek_rect = pygame.Surface((480, 20), pygame.SRCALPHA)
srodek_rect.fill(KOLOR)

srodek_rect = pygame.transform.rotate(srodek_rect, 38)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))

    pygame.draw.rect(win, KOLOR, (100, 100, 400, 20))
    pygame.draw.rect(win, KOLOR, (100, 400, 400, 20))

    rect_rect = srodek_rect.get_rect(center=(300, 260))
    win.blit(srodek_rect, rect_rect.topleft)

    pygame.display.update()

pygame.quit()