from collections import defaultdict

memory = defaultdict(int)



def sum_memory(x,y):
    return memory[(x-1,y)] + memory[(x-1,y+1)] + memory[(x-1,y-1)] + memory[(x+1,y)] + memory[(x+1,y+1)] + memory[(x+1,y-1)] + memory[(x,y+1)] + memory[(x,y-1)]

x, y = 0, 0
memory[(x, y)] = 1
size = 0

run = True

import sys


while run:
    size += 2
    x += 1
    memory[(x,y)] = sum_memory(x,y)
    print(x,y,' = ', memory[(x,y)])
    if memory[(x,y)] > 312051:
        print(memory[(x,y)])
        sys.exit(0)
    for i in range(size-1):
        y += 1
        memory[(x,y)] = sum_memory(x,y)
        print(x,y,' = ', memory[(x,y)])
        if memory[(x,y)] > 312051:
            print(memory[(x,y)])
            sys.exit(0)
    for i in range(size):
        x -= 1
        memory[(x,y)] = sum_memory(x,y)
        print(x,y,' = ', memory[(x,y)])
        if memory[(x,y)] > 312051:
            print(memory[(x,y)])
            sys.exit(0)
    for i in range(size):
        y -= 1
        memory[(x,y)] = sum_memory(x,y)
        print(x,y,' = ', memory[(x,y)])
        if memory[(x,y)] > 312051:
            print(memory[(x,y)])
            sys.exit(0)
    for i in range(size):
        x += 1
        memory[(x,y)] = sum_memory(x,y)
        print(x,y,' = ', memory[(x,y)])
        if memory[(x,y)] > 312051:
            print(memory[(x,y)])
            sys.exit(0)