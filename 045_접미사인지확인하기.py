# ---------------------------------------------------------
# 045 : 접미사인지 확인하기  [문자열]
# https://school.programmers.co.kr/learn/courses/30/lessons/181908
# ---------------------------------------------------------
# 문제:
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
# 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 `my_string`과 `is_suffix`가 주어질 때, 
# `is_suffix`가 `my_string`의 접미사라면 1을, 
# 아니면 0을 return 하는 solution 함수를 작성해 주세요.
# ----------------------------------------
# [제한사항]
# - 1 ≤ `my_string`의 길이 ≤ 100
# - 1 ≤ `is_suffix`의 길이 ≤ 100
# - `my_string`과 `is_suffix`는 영소문자로만 이루어져 있습니다.
# ----------------------------------------
# [입출력 예]
# my_string | is_suffix | result
# "banana" | "ana" | 1
# "banana" | "nan" | 0
# "banana" | "wxyz" | 0
# "banana" | "abanana" | 0
# ----------------------------------------
# [입출력 예 설명]
# 입출력 예 #1
# - 예제 1번에서 `is_suffix`가 `my_string`의 접미사이기 때문에 1을 return 합니다.
# 입출력 예 #2
# - 예제 2번에서 `is_suffix`가 `my_string`의 접미사가 아니기 때문에 0을 return 합니다.
# 입출력 예 #3
# - 예제 3번에서 `is_suffix`가 `my_string`의 접미사가 아니기 때문에 0을 return 합니다.
# 입출력 예 #4
# - 예제 4번에서 `is_suffix`가 `my_string`의 접미사가 아니기 때문에 0을 return 합니다.
# ---------------------------------------------------------
# (여기에 내 풀이)
# 입력: my_string, is_suffix
# 출력: 1 or 0
# 어떻게:
# 1. 임의의 answer [] 만든다
# 2. for 문을 사용한다. 글자수는 모르니까 for i in range(len(my_string))
# 3. is_suffix 값이랑 일치하는게 있는지 비교한다. 일치하면 1, 불일치하면 0을
# 4. 반환한다.

def solution(my_string, is_suffix):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            answer = 1
            return answer
        else:
            answer = 0
    return answer

print(solution("banana", "anana" ))


# 더 깔끔하게
def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            return 1
    return 0


# 메모:
# -----------------------------------------------
# ❓ 질문 45 : 접미사인지 확인하기 - is_suffix가 my_string의 접미사인지 1/0으로 반환
# 😵 페인포인트 :
#    1. i(숫자)와 my_string[i:](문자열)을 혼동 → 비교 대상이 달랐음
#    2. for문이 끝까지 돌면서 answer가 덮어씌워지는 버그 발생
#    3. 찾는 순간 바로 return해야 한다는 것을 몰랐음
#    4. endswith() / startswith() 같은 내장함수 존재를 몰랐음
# 💡 풀이 :
#    1. for i in range(len(my_string))으로 인덱스 반복
#    2. my_string[i:]로 접미사 슬라이싱 후 is_suffix와 비교
#    3. 일치하면 바로 return 1 (덮어씌워지는 버그 방지!)
#    4. for문 다 돌고도 못 찾으면 return 0
#
#    def solution(my_string, is_suffix):
#        for i in range(len(my_string)):
#            if my_string[i:] == is_suffix:
#                return 1
#        return 0
#
#    # 더 짧은 풀이 (endswith 활용)
#    def solution(my_string, is_suffix):
#        return int(my_string.endswith(is_suffix))
#
# ✅ 팁 :
#    - for문 안에서 찾으면 즉시 return → 덮어씌워지는 버그 방지
#    - endswith("문자열") → ~로 끝나니? True/False 반환
#    - startswith("문자열") → ~로 시작하니? True/False 반환
#    - int(True) = 1 / int(False) = 0
#    - True/False 반환하는 함수들 → endswith, startswith, isdigit, isalpha
# -----------------------------------------------