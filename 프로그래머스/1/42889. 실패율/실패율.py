def solution(N, stages):
    answer = [0] * N
    stage_count = [0] * (N + 1)
    
    for i in stages:
        stage_count[i - 1] += 1
        
    remain_count = len(stages)
    
    for index, i in enumerate(stage_count):
        if index < N:
            answer[index] = (index + 1, i / remain_count if remain_count > 0 else 0)
            remain_count -= i
    
    answer.sort(key=lambda x: x[1], reverse=True)

    return list(map(lambda x: x[0], answer))