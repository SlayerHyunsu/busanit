class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    def fly(self):
        print('하늘을 날 수 있다.')

eagle = Eagle()
eagle.fly()

