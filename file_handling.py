# #program 1
# f=open('myfile.txt','r')
# for each in f:
#     print(each)   #read one line at a time
# # print(f)


# #program 2
# f=open('myfile.txt','w')
# f.write('\n now this line is added through program 2')  #if we execute this , it will overwrite all the contents
# f.close()


# #program 3
# #it will read the entire content
# f=open('myfile.txt','r')
# print(f.read())


# #program 4
# #it will read character wise , it reads first 10 characters 
# f=open('myfile.txt','r')
# print(f.read(10))
# print(f.read(5)) #it will read next 5 characters

# #program 5
# f=open('myfile.txt','r')
# if f.mode == 'r':
#     contents=f.read()
#     print(contents)
# f.close()



# #program 6
# f=open('myfile.txt','w')
# for i in range (10):
#     f.write("this line is added %d\r \n"%(i+1))
# f.close


# program 7
# #open file in append mode
# f=open('myfile.txt','a')
# for i in range (10):
#     f.write("another new line is append at the end of file content%d\r \n"%(i+1))
# f.close

# #program 8
# #with()  alongwith write()
# with open('file.txt','w') as f:      # similar as  f=open('myfile.txt','w') and we dont have to close the file manually . it will automatically close the file
#     f.write('hello')
#     for i in range(3):
#         f.write("line #:"+str(i))     


#program 9
#python code to illustrate split() function
with open ('file.txt','r') as file:
    data=file.readline()
    for line in data:
        word=line.split()
        print(word)

