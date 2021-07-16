class person:
       #constructor
    def __init___(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #function
    def printFullName(self):
        print(self.fname+","+self.l)
ob1=person("shetu","das")
print(ob1.fname,ob1.lname)
ob1.printFullName()

ob2=person("ritwik","sen")
ob2.printFullName()

#inheretance
class student(person):
    pass

s1=student('bera','jon')
s1.printFullName()