import pygame
import pygame.camera
from pygame.constants import *
import math
import time

pygame.init()
pygame.camera.init()

pygame.key.set_repeat(500, 10)

surf = pygame.display.set_mode((640, 480), pygame.SRCALPHA, 32)

camlist = pygame.camera.list_cameras()
if camlist:
    cam = pygame.camera.Camera(camlist[0],(640, 480), "RGB")

cam.start()

checkColor = (0, 0, 0)
checkPos = [int(640/2), int(480/2)]
snap = pygame.Surface((640, 480))
thr = 250

checkRect = surf.get_rect()
drawSurf = pygame.Surface((640, 480), pygame.SRCALPHA, 32)
drawSurf = drawSurf.convert_alpha()
posDown = [0, 0]
downPressed = False
picture = True
canTake = False
move = False
run = True
tipPoint = 0.4

Font = pygame.font.Font(None, 20)

while run:
    f = open("../pic/tweet", "a")
    drawSurf.fill((0, 0, 0, 0))
    cam.get_image(snap)
    checkColor = pygame.transform.average_color(snap, pygame.Rect(checkPos[0] + 2, checkPos[1] - 2, 5, 5))
    text1 = Font.render(str(thr), 1, (0, 0, 0))
    text3 = Font.render(str(canTake), 1, (0, 0, 0))
    pygame.draw.circle(drawSurf, (255, 255, 255), checkPos, 2, 1)
    pygame.draw.rect(drawSurf, (255, 255, 255), checkRect, 3)

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            posDown = event.pos
            downPressed = True
            move = True
        if event.type == MOUSEMOTION and downPressed == True:
            if move:
                checkRect.width = 0
                checkRect.height = 0
                move = False

            checkRect.x = posDown[0]
            checkRect.y = posDown[1]
            checkRect.width += event.rel[0]
            checkRect.height += event.rel[1]
        if event.type == MOUSEBUTTONUP:
            downPressed = False
            if math.fabs(posDown[0] - event.pos[0]) <= 10 and math.fabs(posDown[1] - event.pos[1]) <= 10:
                checkPos = posDown
        if event.type == KEYDOWN:
            if event.key == K_MINUS and thr > 0:
                thr -= 1
            if event.key == K_EQUALS and thr < 250:
                thr += 1
            if event.key == K_DELETE:
                canTake = False
            if event.key == K_RETURN:
                canTake = True
            if event.key == K_COMMA and tipPoint > 0:
                tipPoint -= 0.1
                tipPoint = round(tipPoint, 1)
            if event.key == K_PERIOD and tipPoint < 1:
                tipPoint += 0.1
                tipPoint = round(tipPoint, 1)
            if event.key == K_ESCAPE:
                pygame.quit()
                run = False
        if event.type == QUIT:
            pygame.quit()

    thrSurf = pygame.Surface((math.fabs(checkRect.width), math.fabs(checkRect.height)))
    thrSurf.blit(snap, (0, 0), checkRect)
    pixels = pygame.transform.threshold(surf, thrSurf, checkColor, (thr, thr, thr),
                               (0, 0, 0), 0)
    if canTake:
        if pixels / (thrSurf.get_height() * thrSurf.get_width() + 0.0001) <= tipPoint and picture:
            pygame.image.save(snap, time.strftime("../pic/%d,%m,%Y_%H:%M:%S.png"))
            f.write("$" + time.strftime("%d,%m,%Y_%H:%M:%S.png") + "\n")
            picture = False
            pygame.draw.rect(drawSurf, (255, 255, 255), surf.get_rect())
        elif pixels / (thrSurf.get_height() * thrSurf.get_width() + 0.0001) > tipPoint + 0.05:
            picture = True

    text2 = Font.render(str(round(pixels / (thrSurf.get_height() * thrSurf.get_width() + 0.1), 3) * 100) + "%", 1, (0, 0, 0))
    text4 = Font.render(str(round(tipPoint * 100)) + "%", 1, (0, 0, 0))

    surf.blit(snap, (0, 0))
    surf.blit(drawSurf, (0, 0))
    surf.fill((255, 255, 255, 255), pygame.Rect(0, 0, 50, 60))
    surf.blit(text1, (0, 0))
    surf.blit(text2, (0, 15))
    surf.blit(text3, (0, 30))
    surf.blit(text4, (0, 45))

    pygame.display.flip()
    f.close()

__author__ = 'luko'
