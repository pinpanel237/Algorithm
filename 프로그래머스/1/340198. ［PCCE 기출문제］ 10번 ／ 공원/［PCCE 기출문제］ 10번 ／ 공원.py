def solution(mats, park):   
    mats.sort(reverse=True)
    
    for mat in mats:
        for index_y, y in enumerate(park):
            for index_x, x in enumerate(y):
                if x != '-1':  # 사용 못하는 공간일 때
                    continue
                else:  # 돗자리 깔 수 있는 시작점일 때
                    result = True
                    if index_y + mat <= len(park) and index_x + mat <= len(y):  # 남은 범위 안에 돗자리 깔 수 있을 때
                        for i in range(0, mat):  # 돗자리 범위 내 빈 곳 확인
                            for j in range(0, mat):
                                if park[index_y + i][index_x + j] != '-1':
                                    result = False
                        if result:
                            return mat
    return -1