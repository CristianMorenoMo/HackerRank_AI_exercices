def nextMove(n,r,c,grid):
    if True in [('p' in (grid[i])) for i in range(r)]:
        bolean = [('p' in (grid[i])) for i in range(r)]
        r_f = ([i for i in range(len(bolean)) if bolean[i]])[0]
        c_f = [i for i in range(len(grid[r_f])) if (grid[r_f][i]=='p')][0]
        p_p = (r_f,c_f)
    else:
        bolean = [('p' in (grid[i])) for i in range(r,n)]
        r_f = ([i+r for i  in range(len(bolean)) if bolean[i]])[0]        
        c_f = [i for i in range(len(grid[r_f])) if (grid[r_f][i]=='p')][0]
        p_p = (r_f,c_f)
        
    if r-p_p[0] == 0:
        if c-p_p[1] >0 :
            result = 'LEFT'
        else:
            result = 'RIGHT'
    elif r-p_p[0] >0:
        result = 'UP'
    else:
        result = 'DOWN'
    
    return result