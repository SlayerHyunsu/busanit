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
    
# marks = [90,25,67,45,80]
# number = 0
# for mark in marks:
#     # number = number +1
#     number += 1
#     if mark >=70:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         if mark <= 50:
#             print('%d번 학생은 뒤지게 맞습니다.' % number)
#         else:
#             print('%d번 학생은 불합격입니다.' % number)

# marks = [90,25,67,45,80]
# number = 0
# for mark in marks:
#     number =+ 1
#     if mark < 60:
#         continue
#     print('%d번 학생은 합격입니다.' % number)

# a = [1,2,3,4,5,6,7,8,9,10]
# b = range(1,11)

# for i in a:
#     print(i, end=' ')
# print() #print안에 아무것도 없으면 줄바꿈 용도   
# for i in b:
#     print(i, end=' ')
    
# marks = [90,25,67,45,80]
# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print('%d번 학생 축하합니다. 합격입니다.' % (number+1))
    
# for i in range(1,10):
#     for j in range(2,10):
#         print(j,"*",i,'=',i*j, end='   ')
#     print()

# a =[1,2,3,4]
# result =[]
# for num in a:
#     result.append(num*3)
    
# print(result)

# a=[1,2,3,4]
# result=[num*3 for num in a] #리스트'내.in' '포.for'
# print(result)

a=[1,2,3,4]
result = [num*3 for num in a if num % 2 ==0]
print(result)