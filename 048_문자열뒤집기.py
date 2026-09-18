# ---------------------------------------------------------
# 048 : 문자열 뒤집기  [문자열]
# https://school.programmers.co.kr/learn/courses/30/lessons/181905
# ---------------------------------------------------------
# 문제:
# 문자열 `my_string`과 정수 `s`, `e`가 매개변수로 주어질 때, 
# `my_string`에서 인덱스 `s`부터 인덱스 `e`까지를 뒤집은 문자열을 return 하는 
# solution 함수를 작성해 주세요.
# ----------------------------------------
# [제한사항]
# - `my_string`은 숫자와 알파벳으로만 이루어져 있습니다.
# - 1 ≤ `my_string`의 길이 ≤ 1,000
# - 0 ≤ `s` ≤ `e` < `my_string`의 길이
# ----------------------------------------
# [입출력 예]
# my_string | s | e | result
# "Progra21Sremm3" | 6 | 12 | "ProgrammerS123"
# "Stanley1yelnatS" | 4 | 10 | "Stanley1yelnatS"
# ----------------------------------------
# [입출력 예 설명]
# 입출력 예 #1
# - 예제 1번의 `my_string`에서 인덱스 6부터 인덱스 12까지를 뒤집은 문자열은 "ProgrammerS123"이므로 "ProgrammerS123"를 return 합니다.
# 입출력 예 #2
# - 예제 2번의 `my_string`에서 인덱스 4부터 인덱스 10까지를 뒤집으면 원래 문자열과 같은 "Stanley1yelnatS"이므로 "Stanley1yelnatS"를 return 합니다.
# ---------------------------------------------------------
# (여기에 내 풀이)
# 입력: my_string, s, e
# 출력: 인덱스 `s`부터 인덱스 `e`까지를 뒤집은 문자열


def solution(my_string, s, e):
    answer1 = my_string[:s]
    answer2 = my_string[s:e+1]
    answer2 = answer2[::-1]
    answer3 = my_string[e+1:]
    answer = f"{answer1}{answer2}{answer3}"
    return answer

print(solution("Progra21Sremm3", 6, 12))

# 문자열 `my_string`과 정수 `s`, `e`가 매개변수로 주어질 때, 
# `my_string`에서 인덱스 `s`부터 인덱스 `e`까지를 뒤집은 문자열을 return 하는 
# solution 함수를 작성해 주세요.

# 메모:
# -----------------------------------------------
# ❓ 질문 48 : 문자열 뒤집기
# my_string과 정수 s, e가 주어질 때, 인덱스 s부터 e까지(e 포함)를 뒤집은 문자열을 return
# 나머지 부분(s 앞, e 뒤)은 그대로 유지
# 😵 페인포인트 :
# - 슬라이싱을 콤마로 씀 (my_string[s,e]) → 콜론(:)이어야 함
# - reversed()가 바로 문자열을 안 주고 이터레이터(껍데기)만 줘서 헷갈림
# - [s:e+1:-1]처럼 "자르기+뒤집기"를 한 번에 하려다 방향이 꼬임
#   → s가 e보다 작은데 스텝을 -1(후진)로 주면 빈 문자열이 나와버림
# - f-string에 괄호를 그대로 넣어서 출력에 "(", ")"가 섞여 들어감
# - return과 대입(=)을 한 줄에 같이 씀 (return answer = f"...") → 문법 오류
#   (047번에서도 return 빠뜨렸었는데, 이번엔 다른 방식으로 또 걸림)
# 💡 풀이 :
# - 문자열을 세 조각으로 나눠서 생각: 앞부분 + 가운데(뒤집을 곳) + 뒷부분
#   answer1 = my_string[:s]       → 안 건드리는 앞부분
#   answer2 = my_string[s:e+1]    → 뒤집을 가운데 (e까지 포함하려고 +1)
#   answer2 = answer2[::-1]       → 가운데만 뒤집기
#   answer3 = my_string[e+1:]     → 안 건드리는 뒷부분
# - 세 조각을 f-string으로 이어 붙이고, 대입과 return을 분리해서 처리
# ✅ 팁 :
# - 슬라이싱은 무조건 콜론(:), 콤마 아님
# - "자르면서 동시에 뒤집기"는 방향 헷갈리기 쉬우니, 먼저 순방향으로 자르고
#   그 다음 [::-1] 붙이는 2단계 방식이 훨씬 안전함
# - e번째까지 "포함"해서 자르려면 슬라이싱 끝 번호에 +1 해줘야 함
#   (파이썬 슬라이싱은 끝 번호를 포함 안 하니까)
# - return과 대입(=)은 같은 줄에 못 씀 → 계산은 위에서, return은 마지막 줄에 따로
# -----------------------------------------------


# 내 엉망인 답:
#def solution(my_string, s, e):
#    s = int(s)
#    e = int(e)
#    answer = my_string[s,e]
#    answer = reversed(answer)

#print(solution("Progra21Sremm3", 6, 12))