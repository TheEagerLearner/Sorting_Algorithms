import pygame, sys, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 1200
HEIGHT = 640
win_size = (WIDTH, HEIGHT)

pygame.init()

win = pygame.display.set_mode(win_size)
pygame.display.set_caption('Sorting Algorithms')
clock = pygame.time.Clock()

surface1 = pygame.Surface((WIDTH//2, HEIGHT//2))

#width of the bars
n = 2

w = int(surface1.get_width()/n)
h_arr = []
states = []

def maps(num, in_min, in_max, out_min, out_max):
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def bubble_sort(arr, states, counter):
    if counter < len(arr):
        for j in range(len(arr) - 1 - counter):
            if arr[j] > arr[j+1]:
                states[j] = 0
                states[j+1] = 0
                temp = h_arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                states[j] = 1
                states[j+1] = 1
    else:
        print('Done')
        flag = True

def selection_sort(arr, states, counter):
    if counter < len(arr):
        min_idx = counter
        for j in range(counter+1, len(arr)):
            if arr[min_idx] > arr[j]:
                states[j] = 0
                min_idx = j
            else:
                states[j] = 1
                states[min_idx] = 1
        arr[counter], arr[min_idx] = arr[min_idx], arr[counter]
        return False
    else:
        print('Done')
        flag = True
        return flag

def insertion_sort(arr, counter):
    if counter < len(arr):
        key = arr[counter]
        j = counter - 1
        while j >= 0 and key < h_arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        return False
    else:
        print('Done')
        flag = True
        return flag


for i in range(w):
    #height of the bars
    height = random.randint(0, surface1.get_height()//2-10)
    h_arr.append(height)
    states.append(1)

counter = 0
flag = False
startflag = True
while True:
    win.fill(BLACK)

    if flag or startflag:
        pass
    else:
        # flag = bubble_sort(h_arr, states, counter)
        # flag = insertion_sort(h_arr, counter)
        flag = selection_sort(h_arr, states, counter)
        #InsertionSort
        # if counter < len(h_arr):
        #     key = h_arr[counter]
        #     j = counter - 1
        #     while j >= 0 and key < h_arr[j]:
        #         h_arr[j+1] = h_arr[j]
        #         j -= 1
        #     h_arr[j+1] = key
        #Selection Sort
        # if counter < len(h_arr):
        #     min_idx = counter
        #     for j in range(counter+1, len(h_arr)):
        #         if h_arr[min_idx] > h_arr[j]:
        #             states[j] = 0
        #             min_idx = j
        #         else:
        #             states[j] = 1
        #             states[min_idx] = 1
        #     h_arr[counter], h_arr[min_idx] = h_arr[min_idx], h_arr[counter]
        #BubbleSort
        # if counter < len(h_arr):
        #     for j in range(len(h_arr) - 1 - counter):
        #         if h_arr[j] > h_arr[j+1]:
        #             states[j] = 0
        #             states[j+1] = 0
        #             temp = h_arr[j]
        #             h_arr[j] = h_arr[j+1]
        #             h_arr[j+1] = temp
        #         else:
        #             states[j] = 1
        #             states[j+1] = 1
        # else:
        #     print('Done')
        #     flag = True
        counter += 1


    for i in range(len(h_arr)):
        h_ar = maps(h_arr[i], 0, surface1.get_height()//2-10, 20, 255)#
        gap = surface1.get_width() - h_arr[i]
        pygame.draw.rect(surface1, (h_ar//4, h_ar//2, h_ar), pygame.Rect(int(i*n), gap//2, n, h_arr[i]))#h_arr[i]))

    win.blit(surface1, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                startflag = False
    

    pygame.display.flip()
