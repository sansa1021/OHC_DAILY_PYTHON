#import pandas as pd
#data = {
    "order_id": ["ord_1", "ord_2", "ord_3", "ord_4", "ord_5"],
    "product_name": ["핸드크림", "텀블러", "노트북파우치", "비타민", "마우스"],
    "payment_method": ["card", "naver_pay", "card", "bank_transfer", "card"],
    "unit_price": [15000, 25000, 35000, 12000, 45000]
}
#df = pd.DataFrame(data)

#df.loc["payment_method" = "card", "product_name", "unit_price"]
    #result = loc
#print(result)
#ㄴ 멍청한 내가 짠 코드..

#ㄴ 튜터가...수정한 정답 부분


import pandas as pd

# 가상 데이터 생성
data = {
"order_id": ["ord_1", "ord_2", "ord_3", "ord_4", "ord_5"],
"product_name": ["핸드크림", "텀블러", "노트북파우치", "비타민", "마우스"],
"payment_method": ["card", "naver_pay", "card", "bank_transfer", "card"],
"unit_price": [15000, 25000, 35000, 12000, 45000]
}
df = pd.DataFrame(data)
result = df.loc[df["payment_method"] == "card", ["order_id", "product_name", "unit_price"]]
print(result)

