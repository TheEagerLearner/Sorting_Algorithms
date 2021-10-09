import pygame, sys, random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 640
HEIGHT = 480
win_size = (WIDTH, HEIGHT)

pygame.init()

win = pygame.display.set_mode(win_size)
pygame.display.set_caption('Selection Sort Visualization')
clock = pygame.time.Clock()

n = 4

w = int(WIDTH/n)
h_arr = []
state = []
for i in range(w):
    height = random.randint(10, 450)
    h_arr.append(height)
    state.append(1)


counter = 0

def partition(arr, start, end):
    for i in range(start, end):
        state[i] = 0
    i = start
    pivot = arr[end]
    state[start] = 0
    for j in range(start, end):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            state[i] = 1
            i += 1
            state[i] = 0

    arr[i], arr[end] = arr[end], arr[i]
    return i

def quickSort(arr, start, end):
    size = end - start + 1
    stack = [0] * (size) 
  
    # initialize top of stack 
    top = -1
  
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = start 
    top = top + 1
    stack[top] = end 
  
    # Keep popping from stack while is not empty 
    while top >= 0: 
  
        # Pop h and l 
        end = stack[top] 
        top = top - 1
        start = stack[top] 
        top = top - 1
  
        # Set pivot element at its correct position in 
        # sorted array 
        p = partition( arr, start, end ) 
  
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        if p-1 > start: 
            top = top + 1
            stack[top] = start 
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        if p + 1 < end: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = end 

def draw(win, h_arr):
    win.fill((10, 10, 10))
    for i in range(len(h_arr)):
        if state[i] == 0:
            color = RED
        elif state[i] == 2:
            color = GREEN  
        else:
            color = WHITE
        pygame.draw.rect(win, color, pygame.Rect(int(i*n), HEIGHT - h_arr[i], n, h_arr[i]))


end = len(h_arr) - 1
start = 0
size = end - start + 1
stack = [0] * (size) 

top = -1

top = top + 1
stack[top] = 0 
top = top + 1
stack[top] = end 

j = 0

while True:
    win.fill((10, 10, 10))

    if top >= 0: 
        end = stack[top] 
        top = top - 1
        start = stack[top] 
        top = top - 1

        p = partition(h_arr, start, end)
        state[p] = 1 
        if p-1 > start: 
            top = top + 1
            stack[top] = start 
            top = top + 1
            stack[top] = p - 1
    
        if p + 1 < end: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = end 
    else:
        if j < len(h_arr):
            state[j] = 2
            j += 1
        else:
            print('Done')
    
    for i in range(len(h_arr)):
        if state[i] == 0:
            color = RED
        elif state[i] == 2:
            color = GREEN  
        else:
            color = WHITE
        pygame.draw.rect(win, color, pygame.Rect(int(i*n), HEIGHT - h_arr[i], n, h_arr[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    clock.tick(60)
    pygame.display.flip()