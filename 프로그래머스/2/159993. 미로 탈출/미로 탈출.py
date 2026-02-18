from collections import deque

def solution(maps):
    answer = 0
    queue = deque()
    row_size = len(maps)
    col_size = len(maps[0])
    start = [-1, -1]
    lever = [-1, -1]
    
    for r in range(row_size):
        for c in range(col_size):
            if maps[r][c] == 'S':
                start = [r, c]
            elif maps[r][c] == 'L':
                lever = [r, c]
    
    visited_map = [[False] * col_size for _ in range(row_size)]
    queue.append((start, 0))
    visited_map[start[0]][start[1]] = True
    lever_result = bfs(maps, visited_map, queue, 'L')
    if lever_result == -1:
        return -1
    
    queue.clear()
    visited_map = [[False] * col_size for _ in range(row_size)]
    queue.append((lever, 0))
    visited_map[lever[0]][lever[1]] = True
    exit_result = bfs(maps, visited_map, queue, 'E')
    if exit_result == -1:
        return -1
    
    return lever_result + exit_result

def bfs(maps, visited_map, queue, dest):
    row_size = len(maps)
    col_size = len(maps[0])
    
    while queue:
        [row, col], count = queue.popleft()
    
        if maps[row][col] == dest:
            return count
        
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for d_row, d_col in direction:
            next_row = row + d_row
            next_col = col + d_col
            
            if check_boundary(maps, visited_map, next_row, next_col):
                queue.append(([next_row, next_col], count + 1))
                visited_map[next_row][next_col] = True
    return -1
            
def check_boundary(maps, visited_map, next_row, next_col):
    row_size = len(maps)
    col_size = len(maps[0])
    
    if (0 <= next_row and next_row < row_size 
        and 
        0 <= next_col and next_col < col_size
        and
        visited_map[next_row][next_col] == False
        and
        maps[next_row][next_col] != 'X'
       ):
        return True
    return False    