# Class 변수

# a = FourCal(4,2)
# a.first = 4 <- 객체변수
# a.second = 2 <- 객체변수
# b = FourCal(6,2)
# b.first = 6 <- 객체변수
# b.second = 2 <- 객체변수

class Family:
    lastname = "박"

    def setdata(self, firstname):
        self.firstname = firstname

print(Family.lastname)

a = Family()
b = Family()
a.setdata("길동")
b.setdata("찬호")

print(a.lastname, a.firstname)
print(b.lastname, b.firstname)