import pygame as p
p.init()
display=p.display.set_mode((800,600))
p.display.update()
open=True
while open:
    for event in p.event.get():
        if event.type==p.QUIT:
            open=False
p.quit()
quit()