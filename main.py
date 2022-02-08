import sys

import pygame
import requests

FILE_NAME = 'map.png'


class Params:
    def __init__(self, longitude, latitude, spn, l_params):
        self.longitude = longitude
        self.latitude = latitude
        self.spn = spn
        self.l_params = l_params

    def do_dict(self):
        dic = {}
        dic['ll'] = ','.join([str(self.longitude), str(self.latitude)])
        dic['l'] = self.l_params
        dic['spn'] = ','.join([str(self.spn), str(self.spn)])
        return dic


def get_pick(dict_param):
    api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(api_server, dict_param)
    if response:
        with open(FILE_NAME, 'wb') as f:
            f.write(response.content)
    else:
        print("УЖАС!!!! ЧТО_ ТО ПОШЛО НЕ ТАК!!!!")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit()


def draw_interface():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(FILE_NAME), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


longitude = 56.261068
latitude = 58.007368
spn = 0.003
l_params = 'map'

map = Params(longitude, latitude, spn, l_params)
get_pick(map.do_dict())
draw_interface()