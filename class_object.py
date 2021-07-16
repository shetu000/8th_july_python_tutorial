
#press ctrl+shift+p



# class person:
        #contructor
#     def __init___(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
# ob=person("shetu","das")
# print(ob.fname,ob.lname)



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
