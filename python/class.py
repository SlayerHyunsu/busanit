# result=0

# def add(num):
#     global result
#     result +=num
#     return result

# print(add(3))
# print(add(4))

# result1 = 0
# result2 = 0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

# class Cookie:
#     pass

# a = Cookie()
# b = Cookie()

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
    
#     def add(self):
#         result = self.first + self.second
#         return result
    
# a = FourCal()
# # b = FourCal()
      
# a.setdata(4,5) 
# # b.setdata(3,7)
# # print(a.first)
# # print(a.second)
# print(a.add())

class FourCal:
    # ----- 객체명 1 ------
    def __init__(self, first, second):
        self.first = first
        self.second = second
    #-----------------------    
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

#객체명 = 생성자
# ------ 객체명1 ------
a = FourCal(4,2)

print(a.add())

a.setdata(10,2)
print(a.add())

#----------------------
#first = 4, second = 2
# a.setdata(4,2)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

#클래스의 상속

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    #add(), mul(), sub(), div() -> FourCal
    def pow(self):
        result = self.first ** self.second
        return result
#메소드 오버라이딩
class safeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
# a = FourCal(4,0)
# print(a.div())
# a = MoreFourCal(4,2)
# print(a.add())
# print(a.pow())
a = safeFourCal(4,0)
print(a.div())

#클래스 변수
a = FourCal(4,2)

b = FourCal(6,2)