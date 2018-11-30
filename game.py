# Olivia Goodrich (otg5nt) and Camille Favero (caf3wu)

# Game idea: Triangular Tetris (aka Tritris)
# We'll be making a Tetris-like game played on a using six tritrominoes made from a base
# triangle shape, rather than square.

# Optional features: enemy, timer, health meter, multiple levels

import pygame
import gamebox
import random
camera = gamebox.Camera(300, 600)
game_on = False
ticker = 0

# Piece conditions
s = 20
h = (s/2)*(3**0.5)
piece_x = 150
piece_y = 50
piece_speed = 10

# Makes the tritrominoes:
tet1 = gamebox.from_polygon(piece_x, piece_y, "red",
                            (0, 0),
                            (0, -s),
                            (h, -s/2),
                            (h, s/2),
                            (0, s),
                            (-h, s/2),
                            (-h, -s/2)
                            )

tet2 = gamebox.from_polygon(piece_x, piece_y, "yellow",
                            (0, 0),
                            (0, -s),
                            (h, -s/2),
                            (h, s/2),
                            (-h, s*1.5),
                            (-h, s/2)
                            )

tet3 = gamebox.from_polygon(piece_x, piece_y, "green",
                            (0, 0),
                            (0, -s),
                            (h, -s/2),
                            (h, s*1.5),
                            (-h, s/2)
                            )

tet4 = gamebox.from_polygon(piece_x, piece_y, "blue",
                            (0, 0),
                            (0, -s),
                            (h*2, 0),
                            (0, s),
                            (-h, s/2)
                            )

tet5 = gamebox.from_polygon(piece_x, piece_y, "purple",
                            (0, 0),
                            (0, -s),
                            (h, -s*1.5),
                            (h, s/2),
                            (0, s),
                            (-h, s/2)
                            )

tet6 = gamebox.from_polygon(piece_x - 40, piece_y, "orange",
                            (0, -s),
                            (-h, -s/2),
                            (-h, s*1.5),
                            (0, s*2)
                            )

tritrominoes = [tet1, tet2, tet3, tet4, tet5, tet6]



def tick(keys):

    global game_on
    global piece_speed
    global tritrominoes
    global piece_x
    global piece_y

    current_piece = tritrominoes[random.randint(0, 5)]
    # current_piece = tritrominoes[5]

    for i in range(10):
        countdown = int(i)
        timer = gamebox.from_text(150, 300, "Start in: " + str(countdown))

    if game_on:
        if pygame.K_RIGHT in keys:
            piece_x += 10
        if pygame.K_LEFT in keys:
            piece_x -= 10
        piece_y -= piece_speed

    camera.draw(current_piece)
    if ticker <= 300:
        camera.draw(timer)
    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
