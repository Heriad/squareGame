import pygame


class Option:

    cover = False

    def __init__(self, text, position, resolution):
        self.text = text
        self.position = position
        self.set_rect()
        self.draw(resolution)

    def font_rend(self):
        myfont = pygame.font.Font(None, 40)
        self.rend = myfont.render(self.text, 1, self.get_color())

    def get_color(self):
        if self.cover:
            return (74, 74, 74)
        else:
            return (45, 45, 45)

    def set_rect(self):
        self.font_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.position

    def draw(self, resolution):
        self.font_rend()
        resolution.blit(self.rend, self.rect)





