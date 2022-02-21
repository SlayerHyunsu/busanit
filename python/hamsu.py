def add(a,b):   #a,b는 매개변수
    return a+b
# # print(add(5,3))
x = 3
y = 4
c = add(x,y)
print(c)
# 함수를 만들어 놓으면 값이 들어갈 자리에
# 아무 이름을 줘도 된다? 

def eun(a,b):
    result = a + b
    return result
p = eun(3,9)
print(p)


def say():
    return 'Hi'
a = say()
print(a)

def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))

add(5,3)

def say():
    print('Hi')
    
say()

def add(a,b):
    result = a+b
    return result
result = add(5,3)
print(result)

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


result = 0
args = [1,2,3,4,5]
for i in args : 
    result = result + i
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul('add',1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

def add_and_mul(a,b):
    return a+b, a*b
result1, result2 = add_and_mul(3,4)
# result = add_and_mul(3,4)
# print(result) , print(type(result))
print(result1,result2)











