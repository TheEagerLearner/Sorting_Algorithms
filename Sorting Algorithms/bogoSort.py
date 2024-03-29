import pygame, sys, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 720
HEIGHT = 400
win_size = (WIDTH, HEIGHT)

pygame.init()

win = pygame.display.set_mode(win_size)
pygame.display.set_caption('Bogo Sort')
clock = pygame.time.Clock()

#width of the bars
n = 120

w = int(WIDTH/n)
h_arr = []
states = []

def maps(num, in_min, in_max, out_min, out_max):
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

for i in range(w):
    #height of the bars
    height = random.randint(10, 400)
    h_arr.append(height)
    states.append(1)

counter = 0

flag = False

while True:
    win.fill(BLACK)

    if flag:
        if h_arr != sorted(h_arr):
            random.shuffle(h_arr)
        else:
            flag = False

    for i in range(len(h_arr)):
        h_ar = maps(h_arr[i], 0, 400, 20, 255)
        pygame.draw.rect(win, (h_ar//3, h_ar, h_ar//4), pygame.Rect(int(i*n), (HEIGHT - h_arr[i])//2, n, h_arr[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                flag = True 
    
    clock.tick(60)
    pygame.display.flip()
