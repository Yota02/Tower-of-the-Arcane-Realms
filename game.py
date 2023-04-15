import pygame 
import pytmx 
import pyscroll


class Game: 

    def __init__(self):
        self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h ))
        pygame.display.set_caption("Tower of the Arcane Realms")
        
        tmx_data = pytmx.util_pygame.load_pygame('assets/utilitaire/carte/test.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)

        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.is_playing = True
        self.background = 4
        self.pressed = {}

        


    def run(self):
        running = True 

        while running:

            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False