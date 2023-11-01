import pygame
import sys
import math

class Plano:
    def __init__(self,chioce):
        pygame.init()
        self.ancho = 800
        self.alto = 600
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption('Figura')
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.puntos = []
        self.choice = chioce
        self.two_points_added = False

    def dibuja_circulo_con_diametro(self, p1, p2):
        radius = math.dist(p1, p2) / 2
        center = (int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2))
        pygame.draw.circle(self.pantalla , self.black, center, int(radius), 1)

    def dibuja_rectangulo(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        x_left = min(x1, x2)
        x_right = max(x1, x2)
        y_top = min(y1, y2)
        y_bottom = max(y1, y2)
        pygame.draw.rect(self.pantalla, self.black, (x_left, y_top, x_right - x_left, y_bottom - y_top), 1)

    def dibuja_triangulo_rectangulo(self, puntos):
        if len(puntos) == 2:
            a, b = puntos
            x1, y1 = a
            x2, y2 = b
            c_x = x2
            c_y = y1
            vertices = [a, b, (c_x, c_y)]
            pygame.draw.polygon(self.pantalla, self.black, vertices, 1)
    def dibujo(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.two_points_added:
                        x, y = pygame.mouse.get_pos()
                        self.puntos.append((x, y))
                        if len(self.puntos) == 2:
                            self.two_points_added = True

            self.pantalla.fill(self.white)

            pygame.draw.line(self.pantalla, self.black, (self.ancho // 2, 0), (self.ancho // 2, self.alto))
            pygame.draw.line(self.pantalla, self.black, (0, self.alto // 2), (self.ancho, self.alto // 2))

            for point in self.puntos:
                pygame.draw.circle(self.pantalla, self.black, point, 5)

            if len(self.puntos) == 2:
                if self.choice == 1:
                    self.dibuja_circulo_con_diametro(self.puntos[0], self.puntos[1])
                elif self.choice == 2:
                    self.dibuja_rectangulo(self.puntos[0], self.puntos[1])
                elif self.choice == 3:
                    self.dibuja_triangulo_rectangulo(self.puntos)

            pygame.display.flip()

