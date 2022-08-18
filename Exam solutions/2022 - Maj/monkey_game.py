import numpy as np
def monkey_game(x, y, commands):
    position=np.array([x,y])
    commands=commands.split(' ')
    for command in commands:
        if command == 'right':
            position[0]=position[0]+1
        if command == 'jump':
            position[0]=position[0]+1
            position[1]=position[1]+2
        if command == 'left':
            position[0]=position[0]-1
        if command == 'down':
            position[1]=position[1]-1
    return position

print(monkey_game(1,2,'right right jump left down'))

