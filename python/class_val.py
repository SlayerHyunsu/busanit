class Family:
    lastname ="오"

    def setdata(self, firstname):
        self.firstname = firstname
        
a = Family()
b = Family()

a.setdata("이")
b.setdata("이맛꿀단지")
print(a.lastname, a.firstname)
print(b.lastname, b.firstname)
