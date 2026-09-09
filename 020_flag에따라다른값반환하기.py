# ---------------------------------------------------------
# 020 : flag에 따라 다른 값 반환하기  [조건문]
# https://school.programmers.co.kr/learn/courses/30/lessons/181933
# ---------------------------------------------------------
# 문제:
# 두 정수 `a`, `b`와 boolean 변수 `flag`가 매개변수로 주어질 때, 
# `flag`가 true면 `a` + `b`를 false면 `a` - `b`를 return 하는 
# solution 함수를 작성해 주세요.
# ----------------------------------------
# [제한사항]
# - -1,000 ≤ `a`, `b` ≤ 1,000
# ----------------------------------------
# [입출력 예]
# a | b | flag | result
# -4 | 7 | true | 3
# -4 | 7 | false | -11
# ----------------------------------------
# [입출력 예]
# 입출력 예 #1
# - 예제 1번에서 `flag`가 true이므로 `a` + `b` = (-4) + 7 = 3을 return 합니다.
# 입출력 예 #2
# - 예제 2번에서 `flag`가 false이므로 `a` - `b` = (-4) - 7 = -11을 return 합니다.
# ---------------------------------------------------------
# (여기에 내 풀이)
# 문제:
# 두 정수 `a`, `b`와 boolean 변수 `flag`가 매개변수로 주어질 때, 
# `flag`가 true면 `a` + `b`를 false면 `a` - `b`를 return 하는 
# solution 함수를 작성해 주세요.

# if flag == 1  =>  a + b
# if flag == 0  =>  a - b 

def solution(a, b, flag):
    if flag == True: # if flag는 "만약 flag에 들어있는 값이 참(True)이라면"을 검사하는 파이썬 조건문 문법, '==True' 필요없음
        return a + b
    else:
        return a - b 

print(solution(1,2,False))

# 삼항연산자
def solution(a, b, flag):
    return a + b if flag else a - b

print(solution(1,2,False))

# 메모:
