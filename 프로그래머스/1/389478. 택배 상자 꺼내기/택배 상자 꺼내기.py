def solution(n, w, num):
    height = n // w + (n % w != 0 if 1 else 0)
    result = [[] for _ in range(height)]
    answer_index = -1
    
    # 홀수층
    count = 0
    for i in range(0, n, 2 * w):
        for j in range(i, i + w):
            if j == n:
                break
            result[count].append(j + 1)
            if j + 1 == num:
                answer_index = len(result[count]) - 1
        # 빈 공간 -1로 채우기
        if len(result[count]) < w:
            for k in range(w - len(result[count])):
                result[count].append(-1)
        count += 2
        
    # 짝수층
    count = 1
    for i in range(w, n, 2 * w):
        for j in range(i, i + w):
            if j == n:
                break
            result[count].append(j + 1)
            if j + 1 == num:
                answer_index = w - len(result[count])   
        # 짝수층은 결과 반대로
        result[count].sort(reverse=True)
        # 빈 공간 -1로 채우기
        if len(result[count]) < w:
            for k in range(w - len(result[count])):
                result[count].insert(0, -1)
        count += 2
    
    answer = 1
    for i in range(height - 1, -1, -1):
        if result[i][answer_index] == num:
            return answer
        if result[i][answer_index] != -1:
            answer += 1