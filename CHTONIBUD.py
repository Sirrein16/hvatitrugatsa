from pygame import*

okno = display.set_mode((600,600))
game = True
fps = time.Clock()

def gg():
    pass

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    okno.fill((255,255,0))
    fps.tick(60)
    display.update()
