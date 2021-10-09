import pygame as pg, sys, random
from pygame.locals import *


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 720
HEIGHT = 400
win_size = (WIDTH, HEIGHT)

pg.init()

win = pg.display.set_mode(win_size)
pg.display.set_caption('Selection Sort Visualization')
clock = pg.time.Clock()

n = 4

w = int(WIDTH/n)
h_arr = []
state = []
for i in range(w):
    height = random.randint(10, HEIGHT)
    h_arr.append(height)
    state.append(1)

def maps(num, in_min, in_max, out_min, out_max):
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


counter = 0

flag = False


while True:
    win.fill((10, 10, 10))

    if flag:
        if counter < len(h_arr):

            min_idx = counter
            for j in range(counter+1, len(h_arr)):
                if h_arr[min_idx] > h_arr[j]:
                    state[j] = 0
                    min_idx = j
                else:
                    state[j] = 1
                    state[min_idx] = 1
            h_arr[counter], h_arr[min_idx] = h_arr[min_idx], h_arr[counter]

        counter+=1

    # if counter - 1 < len(h_arr):
    #     state[counter - 1] = 2


    for i in range(len(h_arr)):
        h_ar = maps(h_arr[i], 0, HEIGHT, 20, 255)
        pg.draw.rect(win, (h_ar//3, h_ar, h_ar//4), pg.Rect(int(i*n), (HEIGHT - h_arr[i])//2, n, h_arr[i]))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                flag = True 

    
    clock.tick(30)
    pg.display.flip()


