import pygame
import sys
from assets import Dog, Player, Wall, WrongWay, Bone

pygame.init()
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
screen = pygame.display.set_mode((398, 300))
dog = Dog(screen)
wrong_way_list = pygame.sprite.Group()
bone_finish = pygame.sprite.Group()

wr_way_coords = [
[84, 119, 90, 155],
[128, 52, 170, 43],
[165, 163, 58, 100],
[275, 185, 45, 50]
]

for coord in wr_way_coords:
        wr_way = WrongWay(coord[0], coord[1], coord[2], coord[3])
        wrong_way_list.add(wr_way)
        all_sprite_list.add(wr_way)


player = Player(93, 60)
player.walls = wall_list
player.wrong_way = wrong_way_list
player.bone = bone_finish
all_sprite_list.add(dog)
all_sprite_list.add(player)

walls_coords = [
[80, 48, 222, 4],
[302, 48, 3, 204],
[80, 276, 225, 2],
[80, 72, 2, 206],
[80, 72, 20, 2],
[80, 116, 20, 2],
[126, 117, 50, 2],
[104, 96, 47, 2],
[126, 49, 2, 47],
[200, 97, 2, 46],
[200, 141, 90, 2],
[176, 161, 27, 2],
[224, 161, 47, 2],
[246, 161, 2, 46],
[246, 161, 2, 46],
[269, 182, 35, 2],
[272, 202, 2, 50],
[250, 228, 23, 2],
[250, 228, 23, 2],
[271, 249, 26, 2],
]
for coord in walls_coords:
        wall = Wall(coord[0], coord[1], coord[2], coord[3])
        wall_list.add(wall)
        all_sprite_list.add(wall)

bone_coords =[
[313, 234]
]

for coord in bone_coords:
        bone = Bone(coord[0], coord[1])
        bone_finish.add(bone)
        all_sprite_list.add(bone)
global reverse_way
reverse_way = ('d')
def run():
        global reverse_way
        while player.alive == True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_d:
                                        player.change_x =+2
                                        if reverse_way == ('a'):
                                                print('Шарик струсил, и убежал')
                                                player.alive = False
                                        else:
                                                print('Ты на верном пути')
                                                reverse_way = ('d')
                                elif event.key == pygame.K_a:
                                        player.change_x =-2
                                        if reverse_way == ('d'):
                                                print('Шарик струсил, и убежал')
                                                player.alive = False
                                        else:
                                                print('Ты на верном пути')
                                                reverse_way = ('a')
                                elif event.key == pygame.K_s:
                                        player.change_y =+2
                                        if reverse_way == ('w'):
                                                print('Шарик струсил, и убежал')
                                                player.alive = False
                                        else:
                                                print('Ты на верном пути')
                                                reverse_way = ('s')
                                elif event.key == pygame.K_w:
                                        if reverse_way == ('s'):
                                                print('Шарик струсил, и убежал')
                                                player.alive = False
                                        else:
                                                print('Ты на верном пути')
                                                reverse_way = ('w')
                        elif event.type == pygame.KEYUP:
                                if event.key == pygame.K_w:
                                        player.change_x =0
                                elif event.key == pygame.K_s:
                                        player.change_x =0
                                elif event.key == pygame.K_d:
                                        player.change_y =0
                                elif event.key == pygame.K_a:
                                        player.change_y =0
                        all_sprite_list.update()
                        all_sprite_list.draw(screen)
                        pygame.display.flip()

run()