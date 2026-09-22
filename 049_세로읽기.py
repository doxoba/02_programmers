# ---------------------------------------------------------
# 049 : 세로 읽기  [문자열]
# https://school.programmers.co.kr/learn/courses/30/lessons/181904
# ---------------------------------------------------------
# 문제:
# 문자열 `my_string`과 두 정수 `m`, `c`가 주어집니다. 
# `my_string`을 한 줄에 `m` 글자씩 가로로 적었을 때 
# 왼쪽부터 세로로 `c`번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
# ----------------------------------------
# [제한사항]
# - `my_string`은 영소문자로 이루어져 있습니다.
# - 1 ≤ `m` ≤ `my_string`의 길이 ≤ 1,000
# - `m`은 `my_string` 길이의 약수로만 주어집니다.
# - 1 ≤ `c` ≤ `m`
# ----------------------------------------
# [입출력 예]
# my_string | m | c | result
# "ihrhbakrfpndopljhygc" | 4 | 2 | "happy"
# "programmers" | 1 | 1 | "programmers"
# ----------------------------------------
# [입출력 예 설명]
# 입출력 예 #1
# - 예제 1번의 `my_string`을 한 줄에 4 글자씩 쓰면 다음의 표와 같습니다.
# 1열 | 2열 | 3열 | 4열
# i | h | r | h
# b | a | k | r
# f | p | n | d
# o | p | l | j
# h | y | g | c
#     2열에 적힌 글자를 세로로 읽으면 happy이므로 "happy"를 return 합니다.
# 입출력 예 #2
# - 예제 2번의 `my_string`은 `m`이 1이므로 세로로 "programmers"를 적는 것과 같고 따라서 1열에 적힌 글자를 세로로 읽으면 programmers입니다. 따라서 "programmers"를 return 합니다.
# ---------------------------------------------------------
# (여기에 내 풀이)
# 문자열 `my_string`과 두 정수 `m`, `c`가 주어집니다. 
# `my_string`을 한 줄에 `m` 글자씩 가로로 적었을 때 
# 왼쪽부터 세로로 `c`번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
# 입력: 
# 출력: 
# 어떻게: 

def Solution(my_string, m, c):
    m = int(m)
    c = int(c)
    result = []
    for i in range(c-1, len(my_string), m):
        result.append(my_string[i])
    return "".join(result)

print(Solution("ihrhbakrfpndopljhygc", 4, 2))

# 다른 사람의 코드

def solution(s, m, c):
    return s[c-1::m]

# 메모:
# -----------------------------------------------
# ❓ 질문 49 : 세로 읽기 [문자열]
# my_string을 한 줄에 m 글자씩 가로로 적었을 때, 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return
# -----------------------------------------------
# 😵 페인포인트 : 
# - range(시작, 끝, 증감폭) 세 자리에 뭘 넣어야 할지 헷갈림
# - c(몇 번째 열)와 인덱스(0부터 시작)를 그대로 혼동 → c-1로 바꿔야 하는 걸 놓침
# - m을 증감폭 자리에 써야 하는데, 숫자를 하드코딩하거나 끝/증감폭 자리를 서로 바꿔 넣음
# - result.append(값) 순서를 append.result(값)로 반대로 씀 (메서드는 "객체.메서드()" 순서)
# - my_string[i], "".join(result) 처럼 계산만 하고 변수에 저장 안 해서 결과가 날아감
# -----------------------------------------------
# 💡 풀이 :
# 표를 실제로 그리지 않고 인덱스로 흉내냄.
# c번째 열의 첫 글자 인덱스는 (c-1), 그 다음부터는 m씩 증가하는 등차수열.
# → range(c-1, len(my_string), m) 으로 그 인덱스들만 뽑아서
#    for문 돌면서 result 리스트에 my_string[i]를 append,
#    마지막에 "".join(result)로 합쳐서 return.

def solution(my_string, m, c):
    m = int(m)
    c = int(c)
    result = []
    for i in range(c - 1, len(my_string), m):
        result.append(my_string[i])
    return "".join(result)
# -----------------------------------------------
# ✅ 팁 :
# - range(시작,끝,증감폭) 헷갈리면, 추상적으로 말고 원하는 결과의 실제 인덱스를 손으로 먼저 찾아본 뒤
#   그 숫자들 사이 규칙을 변수식으로 바꾸기 (2,7,12 → c-1, +m씩)
# - 메서드 호출은 항상 "리스트.append(값)" 순서
# - 계산한 값은 변수에 담거나 return에 바로 써야 함 — 한 줄에 혼자 써두면 그냥 사라짐
# - 프로그래머스 제출 시 함수명은 소문자 solution
# -----------------------------------------------