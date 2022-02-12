
from tkinter import Variable
from typing import Any
from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Моя первая игра!')



picture = transform.scale(image.loand("fon.jpg"), (700, 500))





run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(picture,(0, 0))

    display.update()
        