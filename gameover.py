import pygame

class Button:
    def __init__(self, menu, x, y, name):
        self.name = name
        self.menu = menu
        self.images = []
        self.path = './assets/misc/buttons'
        self.load_images()
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)
        self.clicked = False
        self.sound = pygame.mixer.Sound('./assets/sound/menu select.wav')
        self.played = False