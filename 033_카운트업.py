# ---------------------------------------------------------
# 033 : 카운트 업  [반복문]
# https://school.programmers.co.kr/learn/courses/30/lessons/181920
# ---------------------------------------------------------
# 문제:
# 정수 `start_num`와 `end_num`가 주어질 때, `start_num`부터 `end_num`까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# ----------------------------------------
# [제한사항]
# - 0 ≤ `start_num` ≤ `end_num` ≤ 50
# ----------------------------------------
# [입출력 예]
# start_num | end_num | result
# 3 | 10 | [3, 4, 5, 6, 7, 8, 9, 10]
# ----------------------------------------
# [입출력 예 설명]
# 입출력 예 #1
# - 3부터 10까지의 숫자들을 담은 리스트 [3, 4, 5, 6, 7, 8, 9, 10]를 return합니다.
# ---------------------------------------------------------
# (여기에 내 풀이)
# 입력: start_num , end_num
# 출력: 리스트
# 어떻게: start_num ~ end num 숫자를 하나하나 담기

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num + 1):
        answer.append(i)
    return answer

print(solution(3,10))

# 다른 사람의 풀이
def solution(start, end):
    return list(range(start, end + 1))

# 메모:
