# c=0
# a = [1,2,3]
# try:
#     c = 10 / 0
#     print(a[1])
# # 0으로 나누기 아...그렇구나
# except ZeroDivisionError:
#     print("0으로 나누기 했습니다.")

# # 인덱스 오류
# except IndexError as e:
#     print(e)
# else:
#     print("오류가 없을 때만 실행됨")
    
# print("항상 실행됨")

try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('잼민이는 출입금지입니다.')
    if age >70:
        print('어차피 놔둬도 자연사야')
    else:
        print('wlecome')
        
