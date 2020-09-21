
import numpy as np

def move_h(x):
    if x<0:
        return 'left'
    elif x==0:
        return 'no move'
    else:
        return 'right'
def move_v(x):
    if x<0:
        return 'upp'
    elif x==0:
        return 'no move'
    else:
        return 'down'

def save_prince(H,V):
    start=True
    while start:
        grid=np.zeros((V,H),dtype=str)
        grid[grid == '0'] = '-' 
        vm,hm = np.random.randint(0,V,size=2)
        grid[vm,hm]='m'
        vp,hp = np.random.randint(0,V,size=2)
        grid[vp,hp]='p'
        rng_win = [x*2 for x in range(-1,2)] 
        win = [(vp,hp+j) for j in  rng_win if j != 0] + [(vp+i,hp) for i in rng_win if i != 0]
        start = (vp,hp) in win
    move=[(i[0]-vm,i[1]-hm) for i in win]
    count_move=[(abs(move[i][0]) + abs(move[i][1])) for i in range(len(move))]
    desi=[i == min(count_move) for i in count_move]
    steps=[move[i] for i in range(len(move)) if desi[i]]
    print(np.array(grid)) 
    for step in steps:
        print(f" {abs(step[0])} steps {move_v(step[0])} and  {abs(step[1])} steps {move_h(step[1]) }")
save_prince(10,10)

