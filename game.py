# Olivia Goodrich (otg5nt) and Camille Favero (caf3wu)

# health code ~ line 136

# Game idea: Xtreme Tetris
# Iterates through multiple levels of modifications as the player progresses,
# including enemy fire, base triangle pieces, and the Flappy gauntlet.

# Optional features: enemy, timer, health meter, multiple levels

import pygame
import gamebox
import random
import t_pieces
camera = gamebox.Camera(320, 640)
ticker = 0

# Game conditions
time_s = 0
score = 0
health = 3
past_pieces = []
game_on = False
trimode = False
enemy_mode = False
if trimode:
    current_piece = t_pieces.tritrominoes[random.randint(0, 5)]  # keeps current_piece from reassigning every frame
else:
    current_piece = t_pieces.tetrominoes[random.randint(0, 6)]

def tribounds_generator(s, h, xaxis, yaxis):
    spikes = int(yaxis/h)
    points_right = []
    points_left = []
    for i in range(0, spikes, -1):
        if i%2 == 0:
            newpoint1_l = (s/2, (i*h)+(yaxis % h))
            newpoint1_r = (xaxis-s/2, (i*h)+(yaxis % h))
            points_left.append(newpoint1_l)
            points_right.append(newpoint1_r)
        else:
            newpoint2_l = (0, (i*h)+(yaxis % h))
            newpoint2_r = (xaxis, (i*h)+(yaxis % h))
            points_left.append(newpoint2_l)
            points_right.append(newpoint2_r)
    return [points_left, points_right]


# Other game elements
floor = gamebox.from_color(160, 690, "grey", 320, 100)
enemy = gamebox.from_image(160, 300, 'bard.png')
enemy.width = 150

if trimode:
    bounds =[
        gamebox.from_polygon(0, 0, "grey", (-50, 0), (50, 640), tribounds_generator(t_pieces.s, t_pieces.h, 320, 640)[0]),
        gamebox.from_polygon(0, 0, "grey", (370, 0), (370, 640), tribounds_generator(t_pieces.s, t_pieces.h, 320, 640)[1])
    ]
else:
    bounds = [gamebox.from_color(-50, 320, "grey", 100, 640), gamebox.from_color(370, 320, "grey", 100, 640)]


def tick(keys):

    global time_s
    global game_on
    global score
    global trimode
    global enemy_mode
    global floor
    global current_piece
    global past_pieces
    global health

    # Timer
    time_s += 1
    #print(time_s)
    if time_s >= 100:
        game_on = True

    # Piece switch (the glitch is here)
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
            current_piece.x += 40
            keys.clear()
        if pygame.K_LEFT in keys:
            current_piece.x -= 40
            keys.clear()
        if pygame.K_DOWN in keys:
            current_piece.y += 40
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

    if enemy_mode:
        if 0 <= enemy.x or enemy.x<= 320:
            enemy.xspeed = -enemy.xspeed
        if 0 <= enemy.y or enemy.y <= 600:
            enemy.yspeed = -enemy.yspeed
        direc_time = random.randint(100, 600)
        interval = time_s % (4*direc_time)
        if interval <= direc_time:
            enemy.x += 10
        elif interval <= 2*direc_time:
            enemy.y += 10
        elif interval <= 3*direc_time:
            enemy.x -= 10
        elif interval <= 4*direc_time:
            enemy.y -= 10

        # if current_piece.touches(enemy):
        #     health -= 1
        # health_bar = [
        #     gamebox.from_color(280, 30, , )
        # ]



    # Drawing
    camera.clear("black")
    camera.draw(floor)
    for bound in bounds:
        camera.draw(bound)
    for piece in past_pieces:
        camera.draw(piece)
    camera.draw(current_piece)
    if game_on and enemy_mode:
        camera.draw(enemy)
        for component in health_bar:
            camera.draw(component)
    timer = gamebox.from_text(camera.x, camera.y, "Start in: " + str(5-int(time_s/20)), 40, "red")
    if not game_on:
        camera.draw(timer)
    camera.display()


ticks_per_second = 20

gamebox.timer_loop(ticks_per_second, tick)
