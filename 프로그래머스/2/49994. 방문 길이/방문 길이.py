def solution(dirs):
    dir_set = set()
    cur_pos = (0, 0)
    next_pos = (-6, -6)
    
    for dir in dirs:
        x, y = cur_pos
        if dir == 'U':
            next_pos = (x, y + 1)
        elif dir == 'D':
            next_pos = (x, y - 1)
        elif dir == 'L':
            next_pos = (x - 1, y)
        elif dir == 'R':
            next_pos = (x + 1, y)
        
        if is_in_boundary(next_pos):
            dir_set.add(tuple(sorted((cur_pos, next_pos))))
            cur_pos = next_pos
    
    return len(dir_set)

def is_in_boundary(next_pos):
    x, y = next_pos
    return -5 <= x <= 5 and -5 <= y <= 5