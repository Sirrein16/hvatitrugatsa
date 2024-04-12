from pygame import*

okno = display.set_mode((600,600))
game = True
fps = time.Clock()

class gameobject(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load('pravo.png'), (w,h))
        self.image2 = transform.scale(image.load("levo.png"), (w,h))
        self.image3 = transform.scale(image.load("verh.png"), (w,h))
        self.image4 = transform.scale(image.load("vniz.png"), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lastx = self.rect.x
        self.lasty = self.rect.y
        self.directon="pravo"
        self.directon='levo'
        self.directon='verh'
        self.directon='vniz'
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
        if self.directon=="pravo":
            okno.blit(self.image, (self.rect.x, self.rect.y))
        if self.directon=="levo":
            okno.blit(self.image2, (self.rect.x, self.rect.y))
        if self.directon=="verh":
            okno.blit(self.image3, (self.rect.x, self.rect.y))
        if self.directon=="vniz":
            okno.blit(self.image4, (self.rect.x, self.rect.y))

class player(gameobject):
    def move(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_a]:
            self.lastx = self.rect.x
            self.rect.x -= 5
            self.directon='levo'
        if kn[K_d]:
            self.lastx = self.rect.x
            self.rect.x += 5
            self.directon="pravo"
        if kn[K_s]:
            self.lasty = self.rect.y
            self.rect.y += 5
            self.directon=="vniz"
        if kn[K_w]:
            self.lasty = self.rect.y
            self.rect.y -= 5
            self.directon='verh'

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    okno.fill((255,255,0))
    fps.tick(60)
    display.update()
