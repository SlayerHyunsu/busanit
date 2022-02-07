# 논리값은 True, False
# money = False
# # if <조건문>:
# if money:
#     print('택시를 타고가라')
# else:
#     print('걸어서 가라')

# money = 2000
# card = True
# if money >=3000 or card:
#     print('택시를 타고 가라')
# else:
#     print('걸어가라')
    
# money = 2000
# card = True
# if money >=3000 and card:
#     print('택시를 타고 가라')
# else:
#     print('걸어가라')

# pocket = ['paper','cellphone','money']
# if 'money' in pocket:
#     print('택시를 타고 가라')
# else:
#     print('걸어가라')
# if 조건문 뼈대만 만들고싶으면 뒤에 pass    
from ipaddress import v4_int_to_packed


pocket = ['paper','cellphone','money']
if 'money' in pocket:
    pass
else:
    pass

# pocket = ['paper','cellphone','money']
# if 'card' in pocket:
#     print('카드꺼내라')
# else:
#     if 'money' in pocket:
#         print('돈꺼내라')
#     else:
#         print('걸어가라ㅋㅋ')

# pocket = ['paper','cellphone','money']
# if 'money' in pocket: pass
# else: print('카드를 꺼내라')

# score=70
# if score >= 60:
#     message = "success"
# else:
#     message = "failure"
    
#  #  참인 경우 if        else 거짓인경우
# message = 'success' if score >=60 else "failure"
# print(message)

# pocket = ['paper','cellphone','money']
# message="택시 타고가라"if 'money' in pocket else"걸어가라"
# print(message)

a=int(input('점수를 적어주세요.'))
if a>=70:
    print('ㅊㅋㅊㅋ')
else:
    print('ㅄㅋㅋ')
    