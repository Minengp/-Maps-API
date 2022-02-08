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

    def increase(self):
        if 0.001 <= self.spn <= 0.01:
            self.spn -= 0.001
        elif 0.01 <= self.spn <= 0.1:
            self.spn -= 0.01
        elif 0.1 <= self.spn <= 1:
            self.spn -= 0.1
        elif 1 <= self.spn <= 10:
            self.spn -= 1
        elif 10 <= self.spn <= 90:
            self.spn -= 10

    def decrease(self):
        if 0.001 <= self.spn <= 0.01:
            self.spn += 0.001
        elif 0.01 <= self.spn <= 0.1:
            self.spn += 0.01
        elif 0.1 <= self.spn <= 1:
            self.spn += 0.1
        elif 1 <= self.spn <= 10:
            self.spn += 1
        elif 10 <= self.spn <= 80:
            self.spn += 10

    def update(self, key):
        if key == pygame.K_PAGEUP:
            self.increase()
        elif key == pygame.K_PAGEDOWN:
            self.decrease()


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


def draw_interface(map):
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            if event.type == pygame.KEYDOWN:
                map.update(event.key)
                get_pick(map.do_dict())
        screen.blit(pygame.image.load(FILE_NAME), (0, 0))
        pygame.display.flip()
    pygame.quit()


longitude = 56.261068
latitude = 58.007368
spn = 0.001
l_params = 'map'

map = Params(longitude, latitude, spn, l_params)
get_pick(map.do_dict())
draw_interface(map)