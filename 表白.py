import pygame
import random
def showMessage(text,size,colour,p):
    fon=pygame.font.Font(None,size)
    sur=fon.render(text,True,colour)
    screen.blit(sur,p)
arrYes=[[60,180]]
pygame.init()
screen=pygame.display.set_mode([300,300])
running=True
nox=190
noy=180
get=False
text="Do you think I'm handsome?"
clock=pygame.time.Clock()
counter=0
countNo=0
counteYes=0
while running:
    screen.fill([10,0,30])
    c = pygame.mouse.get_pos()
    for event in pygame.event.get():
        for b in range(0,len(arrYes)):
            if c[0] > arrYes[b][0] - 20 and c[0] < arrYes[b][0] + 20 and c[1] < arrYes[b][1] + 20 and c[1] > arrYes[b][1] - 20 and event.type ==pygame.MOUSEBUTTONDOWN:
                text ="Thank you. I know I'm handsome"
                get=True
        if c[0] > nox - 20 and c[0] < nox + 20 and c[1] < noy + 20 and c[1] > noy - 20:
            nox = random.randint(0, 250)
            noy = random.randint(0, 250)
            countNo+=1
    if countNo<6:
        showMessage("Yes", 20, [255, 255, 255], [arrYes[0][0],arrYes[0][1]])
        showMessage("No", 20, [255, 255, 255], [nox, noy])
    else:
        counteYes+=1
        for a in range(0, len(arrYes)):
            showMessage("Yes", 20, [255, 255, 255], [arrYes[a][0], arrYes[a][1]])
        if counteYes%20==0:
            arrYes.append([random.randint(0, 250),random.randint(0, 250)])
    if get==True:
        counter+=1
        if counter==180:
            running=False
    showMessage(text,20,[255,100,100],[50,30])
    clock.tick(60)
    pygame.display.flip()
pygame.quit()