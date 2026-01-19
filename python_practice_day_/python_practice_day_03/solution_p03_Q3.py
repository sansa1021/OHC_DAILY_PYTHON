import pandas as pd

# 1. 가상 데이터 생성 (수강생 명단)
data = {
    "student_name": ["김민준", "이서연", "박지후", "최유진", "정하늘"],
    "region": ["SEOUL", "BUSAN", "SEOUL", "DAEGU", "SEOUL"],
    "segment": ["returning", "new", "new", "new", "vip"],
    "signup_date": ["2025-11-18", "2025-11-20", "2025-12-01", "2025-11-25", "2025-11-15"]
}

df = pd.DataFrame(data)

target_students = df.loc[(df["region"] == "SEOUL") & (df["segment"] == "new")]
result = df.sort_values(by = "signup_date", ascending=False)
print(result)
#ㄴ맨처음에 2번째줄 by = 뒤에 signup_date 를 썼다가 target_students 이걸로 바꿨음...내 사고과정을 나도 이해못하겠음. 
#ㄴ무수한 에러를 겪다가 수정하고 해결함!!