from itertools import product 

def solution(n, infection, edges, k):
    answer = 0
    
    # 파이프 열기 순서 경우의 수
    all_pipe_cases = list(product([1, 2, 3], repeat=k))
    
    # 연결된 배양체 리스트 생성
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        start, end, p_type = edge
        graph[start].append((end, p_type))
        graph[end].append((start, p_type))
    
    # 파이프 열었다 닫는 모든 조합 계산
    for case in all_pipe_cases:
        # 감염된 배양체 집합 생성
        infected = set([infection])
        
        # 타입 순서대로 열었다 닫기 반복
        for p_type in case:
            stack = list(infected)
            
            # 연속된 타입 파이프도 처리하도록 반복 수행
            while stack:
                inf = stack.pop();
                for (n_num, n_p_type) in graph[inf]:
                    if p_type == n_p_type and n_num not in infected:
                        infected.add(n_num)
                        stack.append(n_num)
        
        # 감염된 배양체 집합 수와 정답 비교해서 큰 값을 정답으로 설정
        answer = max(answer, len(infected))
    
    return answer