import pygame, sys, random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 640
HEIGHT = 480
win_size = (WIDTH, HEIGHT)

pygame.init()

win = pygame.display.set_mode(win_size)
pygame.display.set_caption('Radix Sort Visualization')
clock = pygame.time.Clock()

n = 4

w = int(WIDTH/n)
h_arr = []
state = []
for i in range(w):
    height = random.randint(10, 450)
    h_arr.append(height)
    state.append(1)

d = 50

counter = 0

def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (d) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ int((index)%10) ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,d): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[ int((index)%10) ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 

def radixSort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10

max1 = max(h_arr)
exp = 1

while True:
    win.fill((10, 10, 10))

    if max1/exp >0:
        countingSort(h_arr,exp) 
        exp *= 10
    
    
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

    
    clock.tick(5)
    pygame.display.flip()