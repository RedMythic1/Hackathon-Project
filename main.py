import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont("freesans",15)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))
class item:  
  def __init__(self, n, v, d):
    self.name = n
    self.value = v
    self.damage = d
    
  
stick = item("stick", 10, 5)
turbotrashpicker = item("turbotrashpicker", 50, 10)
garbagetruck = item("garbagetruck",100,20)
score=0
inventory={}
shop = pygame.image.load('inventory.png')
shop = pygame.transform.scale(shop, (550, 175))
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Trash Simulator")
icon = pygame.image.load('trashcan.png')
gb=pygame.image.load('Green Bin.png')
print(icon)
pygame.display.set_icon(icon)
character = pygame.image.load('character.png')
character = pygame.transform.scale(character, (40,75))
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
aqua=(0,255,255)

while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
      a=pygame.mouse.get_pos()
      x=a[0]
      y=a[1]
     
      if x>459 and x<501 and y>-1 and y<21:
        print("Shop!")
        a=True
         
        while a:
          screen.blit(shop, (0,150))
          pygame.display.update()
          if event.type==pygame.MOUSEBUTTONDOWN:
            a=pygame.mouse.get_pos()
            x=a[0]
            y=a[1]
        
     
            if x>459 and x<501 and y>-1 and y<21:
              print("Shop!")
              a=False
  screen.fill(aqua)
  pygame.draw.rect(screen,red,(460,0,40,20))
  show_text("Shop",463,0,blue)
  show_text("Score:"+str(score),0,0,red)
  pygame.display.update()

      