# ---------------------------------------------------------
# 047 : 접두사인지 확인하기  [문자열]
# https://school.programmers.co.kr/learn/courses/30/lessons/181906
# ---------------------------------------------------------
# 문제:
# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 
# 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
# 문자열 `my_string`과 `is_prefix`가 주어질 때, 
# `is_prefix`가 `my_string`의 접두사라면 1을, 
# 아니면 0을 return 하는 solution 함수를 작성해 주세요.
# ----------------------------------------
# [제한사항]
# - 1 ≤ `my_string`의 길이 ≤ 100
# - 1 ≤ `is_prefix`의 길이 ≤ 100
# - `my_string`과 `is_prefix`는 영소문자로만 이루어져 있습니다.
# ----------------------------------------
# [입출력 예]
# my_string | is_prefix | result
# "banana" | "ban" | 1
# "banana" | "nan" | 0
# "banana" | "abcd" | 0
# "banana" | "bananan" | 0
# ----------------------------------------
# [입출력 예 설명]
# 입출력 예 #1
# - 예제 1번에서 `is_prefix`가 `my_string`의 접두사이기 때문에 1을 return 합니다.
# 입출력 예 #2
# - 예제 2번에서 `is_prefix`가 `my_string`의 접두사가 아니기 때문에 0을 return 합니다.
# 입출력 예 #3
# - 예제 3번에서 `is_prefix`가 `my_string`의 접두사가 아니기 때문에 0을 return 합니다.
# 입출력 예 #4
# - 예제 4번에서 `is_prefix`가 `my_string`의 접두사가 아니기 때문에 0을 return 합니다.
# ---------------------------------------------------------
# (여기에 내 풀이)
# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 
# 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
# 문자열 `my_string`과 `is_prefix`가 주어질 때, 
# `is_prefix`가 `my_string`의 접두사라면 1을, 
# 아니면 0을 return 하는 solution 함수를 작성해 주세요.

# 입력: my_string, is_prefix
# 출력: 
# 어떻게: 
def solution(my_string, is_prefix):
    if len(is_prefix) > len(my_string):
        answer = 0
    answer = 1  # 일단 1이라고 가정
    for i in range(len(is_prefix)):
        if my_string[i]  != is_prefix[i] :
            answer = 0
    return answer

print(solution("banana","an"))




# 메모:

# -----------------------------------------------
# ❓ 질문 47 : 접두사인지 확인하기
# my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사면 1, 아니면 0 return
# 😵 페인포인트 :
# - 이중 for문(my_string 글자 × is_prefix 글자)으로 접근해서 순서 개념이 사라짐
#   → 아무 자리에서나 글자가 겹치면 매치되는 것처럼 잘못 판단
# - len(is_prefix)를 for문에 바로 넣음 (정수는 반복 불가, range() 필요한 걸 놓침)
# - 인덱스 i는 만들어놓고 실제 비교는 [0]으로 고정해서 매번 첫 글자만 비교됨
# - is_prefix가 my_string보다 더 긴 경우(예: "banana" vs "bananan") IndexError 발생
#   → my_string에 없는 자리까지 인덱스로 조회하려고 해서 터짐
# - 이 예외를 막으려고 안전장치(guard)를 넣었는데,
#   처음엔 answer = 0만 세팅하고 코드가 계속 아래로 흘러가서 소용없었음
#   → break를 써보려다 에러 (break는 반복문 전용, 여긴 반복문 진입 전이라 빠져나갈 게 없음)
# 💡 풀이 :
# - 본 로직: answer = 1 로 "일단 접두사 맞다고 가정"하고 시작
#   range(len(is_prefix))로 같은 자리 번호(i)를 뽑아
#   my_string[i] != is_prefix[i] 이면 answer = 0 으로 뒤집기
# - 예외 처리: for문 들어가기 전에 "is_prefix가 my_string보다 길면
#   비교할 필요도 없이 바로 0" 이라는 안내데스크(guard clause)를 맨 앞에 세움
#   → return 0 으로 그 즉시 함수를 끝내버려서, 뒤에 있는 for문 자체를 아예 안 타게 만듦
# ✅ 팁 :
# - "몇 번 돌지"는 range(len(...))로 번호를 뽑아야 함 — len() 자체는 숫자 하나라 반복 불가
# - 두 문자열을 "같은 자리끼리" 비교할 땐 인덱스 하나(i)로 양쪽을 동시에 찌르는 구조
#   (이름표 검사기 비유: 도장 글자를 왼쪽부터 한 칸씩, 같은 순번끼리만 대조)
# - break vs return 차이 명확히!
#   · break  = 반복문(for/while) 하나만 빠져나감
#   · return = 함수 전체를 즉시 끝내고 값까지 들고 나감
# - 인덱스 에러가 날 만한 조건은, 본 로직 들어가기 전에 맨 앞에서 먼저 걸러내기
#   (guard clause: "조건 안 맞으면 일찍 return하고 끝내기" 패턴)
# -----------------------------------------------

# 내 엉뚱한 브레인스토밍:
#def solution():
#    answer = 0
#    for i in my_string:
#        for j in is_prefix:
#            if i[1:array(len(i))-1] == j[1:array(len(j))-1]:
#                answer = 1
