def solution(video_len, pos, op_start, op_end, commands):
    video_len = min_sec_to_sec(video_len)
    pos = min_sec_to_sec(pos)
    op_start = min_sec_to_sec(op_start)
    op_end = min_sec_to_sec(op_end)
    
    # 사용자 입력 반복
    for command in commands:
        # 현재 위치가 오프닝 구간일 때
        if op_start <= pos and pos <= op_end:
            pos = op_end
        
        # 10초 전으로 이동일 때
        if command == 'prev':
            # 현재 위치가 10초 미만일 때
            if pos < 10:
                # 영상 처음 위치로 이동
                pos = 0
            # 10초 미만이 아닐 때
            else:
                # 재생위치 10초 전으로 이동
                pos -= 10
        
        # 10초 후로 이동일 때
        if command == 'next':
            # 동영상의 남은 시간이 10초 미만일 때
            if video_len - pos < 10:
                # 영상의 마지막 위치로 이동
                pos = video_len
            # 10초 미만이 아닐 때
            else:
                # 재생위치 10초 후로 이동
                pos += 10
    
    # 현재 위치가 오프닝 구간일 때
    if op_start <= pos and pos <= op_end:
        pos = op_end
    
    return sec_to_min_sec(pos)

# mm:ss 형식을 숫자 ss로 변경
def min_sec_to_sec(min_sec):
    return 60 * int(min_sec.split(':')[0]) + int(min_sec.split(':')[1])

# ss 형식을 mm:ss로 변경
def sec_to_min_sec(sec):
    return str(sec // 60).zfill(2) + ':' + str(sec % 60).zfill(2)