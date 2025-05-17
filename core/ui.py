import pygame, settings
pygame.font.init()
FONT = pygame.font.Font(settings.FONT_PATH, settings.FONT_SIZE)

def draw_text(surface, text, x, y, w):
    words = text.split(" ")
    line, space, h = "", 4, 0
    for word in words:
        test = line + word + " "
        img = FONT.render(test, True, settings.TEXT_COLOR)
        if img.get_width() > w:
            surface.blit(FONT.render(line, True, settings.TEXT_COLOR), (x, y+h))
            line, h = word + " ", h + img.get_height() + 4
        else:
            line = test
    surface.blit(FONT.render(line, True, settings.TEXT_COLOR), (x, y+h))

def load_avatar():
    idle  = pygame.image.load("assets/img/avatar_idle.png").convert_alpha()
    talk  = pygame.image.load("assets/img/avatar_talk.png").convert_alpha()
    return idle, talk
