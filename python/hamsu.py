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


# def say_myself(name, old, man=True): 
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % old) 
#     if man: 
#         print("남자입니다.")
#     else: 
#         print("여자입니다.")

# say_myself('이현수',74, True)

# say_myself('최은수',69, True)

a = 1
def vartest(a):
    a = a+1
    print('함수안의 a의 값 %d' % a)
    
vartest(a)
print('함수 밖의 a의 값 %d' % a)

a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a) 
print(a)

for i in range(10):
    print(i, end=' ')


















