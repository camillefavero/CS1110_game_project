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
trimode = True
enemy_mode = False
if trimode:
    current_piece = t_pieces.tritrominoes[random.randint(0, 5)]  # keeps current_piece from reassigning every frame
else:
    current_piece = t_pieces.tetrominoes[random.randint(0, 6)]

def triwalls_generator(s, h, xaxis, yaxis):
    spikes = []
    shapes = []
    for i in range(yaxis):
        spike = yaxis-2*h*i
        spikes.append(spike)
    for spike in spikes:
        shape_l = \
            gamebox.from_polygon(0, spike, "grey",
                            (0, 0), (-t_pieces.s, 0), (-t_pieces.s, -2*t_pieces.h), (0, -2*t_pieces.h), (t_pieces.s/2, -t_pieces.h))
        shape_r = \
            gamebox.from_polygon(xaxis, spike, "grey",
                            (0, 0), (t_pieces.s, 0), (t_pieces.s, -2*t_pieces.h), (0, -2*t_pieces.h), (-t_pieces.s/2, -t_pieces.h))
        shapes.append(shape_l)
        shapes.append(shape_r)
    return shapes


# Other game elements
floor = gamebox.from_color(160, 690, "grey", 320, 100)
enemy = gamebox.from_image(160, 300, 'bard.png')
enemy.width = 150

if trimode:
    walls = triwalls_generator(t_pieces.s, t_pieces.h, 320, 640)
else:
    walls = [gamebox.from_color(-50, 320, "grey", 100, 640), gamebox.from_color(370, 320, "grey", 100, 640)]


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

    # Piece switch
    def dead(p):
        p.yspeed = 0
        past_pieces.append(p)
    for wall in walls:
        if current_piece.touches(wall):
            current_piece.move_to_stop_overlapping(wall)
            current_piece.xspeed = 0
    if current_piece.touches(floor):
        current_piece.move_to_stop_overlapping(floor)
        dead(current_piece)
        if not trimode:
            current_piece = t_pieces.tetrominoes[random.randint(0, 6)]
        else:
            current_piece = t_pieces.tritrominoes[random.randint(0, 5)]
    for piece in past_pieces:
        if current_piece.touches(piece):
            dead(current_piece)
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
    for wall in walls:
        camera.draw(wall)
    for piece in past_pieces:
        camera.draw(piece)
    camera.draw(current_piece)
    if game_on and enemy_mode:
        camera.draw(enemy)
        # for component in health_bar:
        #     camera.draw(component)
    timer = gamebox.from_text(camera.x, camera.y, "Start in: " + str(5-int(time_s/20)), 40, "red")
    if not game_on:
        camera.draw(timer)
    camera.display()


ticks_per_second = 20

gamebox.timer_loop(ticks_per_second, tick)
