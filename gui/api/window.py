import sys
sys.path.append('../res')

import pygame
from click import ClickHandler
from colors import color_list

class Window():


    def __init__(self, width, height, caption='Window', background=color_list['white']):
        pygame.init()
        pygame.display.set_caption(caption)
        self.surface = pygame.display.set_mode((width, height))
        self.surface.fill(background)
        self.click_handlers = []
        self.key_handlers = []


    def draw_rect(self, x, y, width, height, color):
        pygame.draw.rect(self.surface, color, (x, y, width, height))
        return (x, y, width, height)


    def draw_textbox(self, x, y, text, color, size=25, action=None, 
                    fontstyle=pygame.font.get_default_font(), underline=False, 
                            bold=False, italic=False):
        text_builder = pygame.font.SysFont(fontstyle, size)
        text_builder.set_underline(underline)
        text_builder.set_italic(italic)
        text_builder.set_bold(bold)
        text_builder.set_underline(underline)
        text_surface = text_builder.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.surface.blit(text_surface, text_rect)

        handler = ClickHandler(text_rect, action)
        self.add_click_handler(handler)

        return text_rect


    def add_click_handler(self, handler):
        self.click_handlers.append(handler)


    def add_key_handler(self, handler):
        self.key_handlers.append(handler)


    def show(self):
        run = True
        while run:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                else:
                    if pygame.mouse.get_pressed()[0]:
                        try:
                            event.pos
                        except AttributeError:
                            print('Mouse pointer outside window')
                        else:
                            for handler in self.click_handlers:
                                handler.handle(event.pos)

                    keys = pygame.key.get_pressed()
                    for handler in self.key_handlers:
                        handler.handle(keys)

        pygame.quit()



if __name__ == '__main__':
    window = Window(800, 600)
    arguments = {'window': window, 'x': 0, 'y': 0, 'width':100, 'height':100, 
            'color': color_list['black']}
    callable = lambda window, x, y, width, height, color: window.draw_rect(x, y, 
            width, height, color)
    window.draw_textbox(300, 300, 'Hello World!', color_list['dark_gray'], 26, action=
            {'callable': callable, 'arguments': arguments}, italic=True, underline=True)
    window.show()
