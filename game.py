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
time_s = 0
score = 0
game_on = False
trimode = True
if trimode:
    current_piece = t_pieces.tritrominoes[random.randint(0, 5)]  # keeps current_piece from reassigning every frame
else:
    current_piece = t_pieces.tetrominoes[random.randint(0, 6)]

# Other game elements
floor = gamebox.from_color(150, 650, "grey", 300, 100)
bounds = [gamebox.from_color(0, 300, "grey", 0, 600), gamebox.from_color(300, 300, "grey", 0, 600)]

def tick(keys):

    global time_s
    global game_on
    global score
    global trimode
    global floor
    global current_piece

    # Timer
    time_s += 1
    #print(time_s)
    if time_s >= 100:
        game_on = True

    past_pieces = []
    current_piece.move_to_stop_overlapping(floor)
    for bound in bounds:
        current_piece.xspeed = 0
        current_piece.move_to_stop_overlapping(bound, 1, 1)
    if current_piece.touches(floor):
        current_piece.yspeed = 0
        past_pieces.append(current_piece)
        if not trimode:
            current_piece = t_pieces.tetrominoes[random.randint(0, 6)]
        else:
            current_piece = t_pieces.tritrominoes[random.randint(0, 5)]

    # Key Controls
    if game_on:
        if pygame.K_RIGHT in keys:
            current_piece.x += 20
        if pygame.K_LEFT in keys:
            current_piece.x -= 20
        if pygame.K_DOWN in keys:
            current_piece.y += 20
        if time_s % 20 == 0 and not (pygame.K_DOWN in keys):
            current_piece.y += 2*t_pieces.s
        # ROTATIONS
        if not trimode:
            if pygame.K_UP in keys:
                current_piece.rotate(90)
                keys.clear()
            if pygame.K_SPACE in keys:
                current_piece.rotate(-90)
                keys.clear()
        else:
            if pygame.K_UP in keys:
                current_piece.rotate(60)
                keys.clear()
            if pygame.K_SPACE in keys:
                current_piece.rotate(-60)
                keys.clear()

    # Drawing
    camera.clear("black")
    camera.draw(floor)
    for bound in bounds:
        camera.draw(bound)
    camera.draw(current_piece)
    for piece in past_pieces:
        camera.draw(piece)
    timer = gamebox.from_text(150, 300, "Start in: " + str(5-int(time_s/20)), 40, "red")
    if not game_on:
        camera.draw(timer)
    camera.display()


ticks_per_second = 20

gamebox.timer_loop(ticks_per_second, tick)
