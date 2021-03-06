''' 프로그래머스>코딩테스트 연습>깊이/너비 우선 탐색(DFS/BFS)>타겟 넘버(level2) '''
'''
BFS, 이진트리구조
큐에 numbers의 원소(양수, 음수)를 각각 더한 값들을 넣고
마지막에 큐에서 값들을 빼내면서 target과 같은 값인지 검사한다. 
'''
from collections import deque

def solution(numbers, target):
    return bfs(numbers, target)

def bfs(numbers, target):
    result = 0
    q = deque()
    q.append(numbers[0])
    q.append(-numbers[0])
    for i in range(1, len(numbers)):
        for j in range(2 ** i):
            n = q.popleft()
            q.append(n + numbers[i])
            q.append(n - numbers[i])
    while q:
        n = q.popleft()
        if n == target:
            result += 1
    return result   
