# Olivia Goodrich (otg5nt) and Camille Favero (caf3wu)

# Game idea: Xtreme Tetris
# Iterates through multiple levels of modifications as the player progresses,
# including enemy fire, base triangle pieces, and the Illuminati.

# Optional features: enemy, timer, health meter, multiple levels

import pygame
import gamebox
import random
import t_pieces
camera = gamebox.Camera(300, 600)
ticker = 0

# Game conditions
countdown = 180
score = 0
game_on = False
trimode = False
piece_selector = random.randint(0, 5)

# Other game elements
floor = gamebox.from_color(150, 605, "grey", 300, 10)

def tick(keys):

    global countdown
    global game_on
    global score
    global trimode
    global floor

    # Timer
    if not game_on:
        countdown -= 1
        if countdown == 0:
            game_on = True

    if trimode:
            current_piece = t_pieces.tritrominoes[piece_selector]
    else:
        current_piece = t_pieces.tetrominoes[piece_selector]

    if current_piece.touches(floor):
        current_piece.move_to_stop_overlapping()
        if current_piece in t_pieces.tetrominoes:
            current_piece = t_pieces.tetrominoes[random.randint(0, 6)]
        else:
            current_piece = t_pieces.tritrominoes[random.randint(0, 5)]

    if game_on:
        if pygame.K_RIGHT in keys:
            t_pieces.piece_x += 10
        if pygame.K_LEFT in keys:
            t_pieces.piece_x -= 10
        t_pieces.piece_y -= t_pieces.piece_speed

    # Drawing
    camera.clear("black")
    camera.draw(floor)
    camera.draw(current_piece)
    timer = gamebox.from_text(150, 300, "Start in: " + str(int(countdown/30)), 40, "red")
    if not game_on:
        camera.draw(timer)
    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
