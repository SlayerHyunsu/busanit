# for 변수 in 리스트(또는 튜플, 문자열):
# 수행할 문장 1
# 수행할 문장 2

# test_list = ["one",'two','three']
# for i in test_list:
#     print(i)

# a=[(1,2),(3,4),(5,6)]
# for (first, last) in a:
#     print(first+last)

# a= [(1,2),(3,4),(5,6)]
# for i in a:
#     print(i)
    
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number +1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)
    else:
        if mark <= 50:
            print('%d번 학생은 뒤지게 맞습니다.' % number)
        else:
            print('%번 학생은 불합격입니다.' % number)
