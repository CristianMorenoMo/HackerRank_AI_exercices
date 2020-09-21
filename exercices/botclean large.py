def grid_1(V,H):
    """
    2:dirty
    0: clear
    """
    grid=np.zeros((V,H))
    r = np.random.rand(V,H)
    r[r<0.1]=2
    g=(grid + r)
    g[g!=2]= 0
    return g
def start_boot(H,V):
    hb = np.random.randint(0,H)
    vb = np.random.randint(0,V)
    return (hb,vb)
def clear(grid,p_boot):
    if grid[p_boot]== 2:
        grid[p_boot]=-1   
        print('clear')
        return True
    else:
        return False
def all_solve(grid,p_boot):
    hb,vb = p_boot
    h,v = grid.nonzero() 
    move = [(hb-h[i],vb-v[i]) for i in range(len(v)) ]
    count_move = [(abs(move[i][0]) + abs(move[i][1])) for i in range(len(move))]
    bool_val = [i == min(count_move) for i in count_move]
    steps = [move[i] for i in range(len(move)) if bool_val[i]]
    return steps, move, count_move
def move(n_ale,rc_des,grid,steps,p_boot):
    hb,vb = p_boot
    if rc_des==1:
        if steps[n_ale][rc_des]<0:    
                vb += -1
                print('left')
        else:
                vb += 1
                print('right')
    else:
        if steps[n_ale][rc_des]<0:    
            hb += 1
            print('down')
        else:
            hb += -1
            print('up')
    return (hb,vb)


    grid=grid_1(10,10)
p_boot=start_boot(10,10)
print(f"p_boot")
if clear(grid,p_boot):
    print('')
else:
    steps=all_solve(grid,p_boot)[0]
    n_ale=np.random.randint(0,len(steps))
    grid[p_boot]=3
    print(grid)
    rc_des=np.random.randint(0,2)
    p_boot=move(n_ale,rc_des,grid,steps,p_boot)
print(p_boot)
