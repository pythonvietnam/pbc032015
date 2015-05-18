class Person:
    pcount = 0
    def __init__(self, name="Nguyen Cong Duc"):
        self.name = name
        print "Da them nguoi", self.name
        Person.pcount += 1
    def printpop():
        print "Dan so la: ", Person.pcount
        
class Vnpeople(Person):
    quocgia = "Vietnam"
    quocca = "Tien quan ca"
    
    def printpop():
        print "Co them 1 nguoi viet nam"
        
a = Person()
a.printpop()

#b = Vnpeople()
#b.printpop
#a.printpop


