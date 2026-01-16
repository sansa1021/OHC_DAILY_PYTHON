# --- 1. 함수(자판기) 만들기 ---
def check_length(word):
    # 글자 수(len)가 2로 나누어 떨어지면 짝수!
    if len(word) % 2 == 0:
        return "짝수입니다"  # 결과를 툭 뱉어냄
    else:
        return "홀수입니다"
#ㄴ뜬금없이 len이 튀어나왔다. 개수를 세는 함수라는것을 방금 기억해냈다.

# --- 2. 함수 사용하기 (손님) ---
# 사용자에게 단어 입력받기
user_input = input("단어를 입력하세요: ")

# 함수 호출! (자판기에 단어 넣기)
# 돌아온 결과(return 값)를 result 변수에 받음
result = check_length(user_input)

# 최종 결과 출력
print(f"입력하신 단어는 {result}")