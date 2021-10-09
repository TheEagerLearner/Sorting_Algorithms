import pygame, sys, random

WIDTH = 720
HEIGHT = 400

pygame.init()

win  = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Insertion Sort')
clock = pygame.time.Clock()

# Bar Width
n = 4
w = int(WIDTH/n)

h_arr = []

def maps(num, in_min, in_max, out_min, out_max):
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

for i in range(w):
    h_arr.append(random.randint(10, 400))

counter = 0
j = 0

flag = False

while True:
    win.fill((10, 10, 10))

    if flag:
        if counter < len(h_arr):
            key = h_arr[counter]
            j = counter - 1
            while j >= 0 and key < h_arr[j]:
                h_arr[j+1] = h_arr[j]
                j -= 1
            h_arr[j+1] = key
        else:
            print('Done')
        counter+=1

    # for i in range(len(h_arr)):
        # pygame.draw.rect(win, (255, 255, 255), (i*n, HEIGHT - h_arr[i], n, h_arr[i]))
    for i in range(len(h_arr)):
        # if states[i] == 0:
        #     color = (255, 0, 0)
        # elif states[i] == 2:
        #     color = (0, 255, 0)
        # else:
        #     color = WHITE
        h_ar = maps(h_arr[i], 0, 400, 20, 255)
        # gap = win.get_height() - h_arr[i]
        # pygame.draw.rect(win, (h_ar//4, h_ar, h_ar//2), pygame.Rect(int(i*n), gap//2, n, h_arr[i]))
        pygame.draw.rect(win, (h_ar//3, h_ar, h_ar//4), pygame.Rect(int(i*n), (HEIGHT - h_arr[i])//2, n, h_arr[i]))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RETURN:
                flag = True 

    clock.tick(60)
    pygame.display.flip()


        










































































































# import pygame as pg, sys, random

# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# WIDTH = 640
# HEIGHT = 480
# win_size = (WIDTH, HEIGHT)

# pg.init()

# win = pg.display.set_mode(win_size)
# pg.display.set_caption('Insertion Sort Visualization')
# clock = pg.time.Clock()

# n = 4

# w = int(WIDTH/n)
# h_arr = []
# state = []
# for i in range(w):
#     height = random.randint(10, 450)
#     h_arr.append(height)
#     state.append(1)


# counter = 0


# while True:
#     win.fill((10, 10, 10))

#     if counter < len(h_arr):
#         key = h_arr[counter]
#         j = counter - 1
#         while j >= 0 and key < h_arr[j]:
#             h_arr[j+1] = h_arr[j]
#             j -= 1
#         h_arr[j+1] = key
#     else:
#         print('Done')
#     counter+=1

#     for i in range(len(h_arr)):
#         if state[i] == 0:
#             color = RED
#         elif state[i] == 2:
#             color = GREEN  
#         else:
#             color = WHITE
#         pg.draw.rect(win, color, pg.Rect(int(i*n), HEIGHT - h_arr[i], n, h_arr[i]))

#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit()

#     clock.tick(30)
#     pg.display.flip()



