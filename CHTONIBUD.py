from pygame import*

okno = display.set_mode((600,600))
game = True

while game:
  for e.type == event.get():
    if e.type == QUIT:
      game = False
  fps.tick(60)
  display.update()
