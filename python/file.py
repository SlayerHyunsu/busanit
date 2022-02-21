# #파일 열기 / w = 쓰기 , a = 내용 추가 , r = 읽기
# f = open('python/새파일.txt', 'r')

# # for i in range(1, 11):
# #     data = "%d번째 줄입니다.\n" % i
# #     f.write(data)
# # # \n: 줄바꿔줌/ 이거 안쓰면 내용이 한줄로 다 써짐

# # for i in range(1,11): # 몇줄인지 알 경우

# # while True:
# #     line = f.readline()
# #     if not line: break
# #     print(line, end='')


# # readlines 함수 
# # lines = f.readlines()
# # for line in lines:
# #     print(line, end='')

# #read 함수
# data = f.read()
# print(data)

# # with문과 함께 사용하기
# f.write()


# #파일 닫기
# f.close()

# f = open('새파일.txt','w')
# f.write('Life is to short, you need python')
# f.close()

# with open('foo.txt','w') as f:
#     f.write('Life is to short, you need python')
    
