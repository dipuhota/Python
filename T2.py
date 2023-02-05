# 1
#DSA string

# string="dipu"

# for i in range(len(string)):
#     if i%2==0:
#        print(string[i])


# for i in string:
#     print(i)



# print(string[len(string)-1])
# print(string[0:3])

# print(string[-3:-1])

# print(string[1:3])
# print(string[-3:-2])



# 2
#Reverseing string
# string="dipuhota"
# rev_str=""
# print(string)

# print(string[::-1])

# # print(string[3:len(string)-1])

# # print(string[:])




# for i in range(len(string)-1,-1,-1):
#     # print(string[i])
#     rev_str+=string[i]
# # print(rev_str)






# 3
# Functions

# string="dipuhota"
# print(string.replace("d","x"))
# print(string)
# print(string.capitalize())
# print(string.count("d"))
# print(string.isalpha)


# alpha,num="",""


# for i in string:
#     if i.isdigit():
#       num+=i

# else:
#     alpha+=i

# print(int(num),alpha)






# 5
#List

# mylist=[1,True,"Hello",7.0]


# print(mylist[len(mylist)-1])
# print(mylist[-1])
# print(mylist[-1])


# for i in range (len(mylist)):
#     print(i,mylist)

# print(mylist[::-1])
# for i in mylist:
#     print(i)






# 6
# 2D List

# mylist=[[1,2,3,4],
#        [5,6,7,8],
#        [9,8,7,6]]

#x=mylist[0]
# print(mylist[0][0])

# print(len(mylist))
# for i in mylist:
    #   for j in i:
#     print(j)








# 7
# use defined input

# mylist=[5,2,4,3,4]
# print(mylist.count(4))

# n=int(input("Enter size of list :"))


# n= int(input())
# for i in range(n):
#     x=input()
#     mylist.append(x)
# print(mylist)







# 8
# students = {
#     1 : {
#         "name" : "mike",
#         "age" : 20,
#         "gender" : "male",
#         "grade" : {
#         "10" : 92,
#         "12" : 88,
#         "B-Tech" : 85
#         }
#     },
#     2 : {
#         "name" : "lucy",
#         "age" : 20,
#         "gender" : "female",
#         "grade" : {
#         "10" : 93,
#         "12" : 87,
#         "B-Tech" : 84
#         }
#     }
# }

# for i in students.keys():
#     # print(students[i])
#     for j in students[i]:
#         print(j, students[i][j])
#     print()
#     print()







# 8

# student  = {
#     "name" : "max",
#     "age" : 21,
#     "university" : "ABC University"
# }

# # print(student.keys())

# # print(student["name"])

# for i in student.keys():
#     print(i, student[i])


