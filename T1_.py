#1
# n=int(input())
# for i in range(n):
#     #upper loop
#     for j in range(n-i-1):
#         print(" ",end=" ")
#         #lower loop
#     for k in range(i+1):
#         print("*",end=" ")
#     print()


#2
# n=int(input())

# for i in range(n):
#     # print(i+1)
#     for j in range(i+1):
#         print("*",end="")
#     print()

#3
# n=int(input())

# for i in range(n):
#     # print(i+1)
#     for j in range(i+1):
#         print("*",end="")
#         print("hi",end="")
#     print()


#4
# n=int(input())

# for i in range(n,0,-1):
#     # print(i)
#     for j in range(i):
#         print("*",end="")
#     print()


#5
# n=int(input())

# for i in range(n):

#     # loop
#     for j in range(n-i-1):
#         print("",end="")
#     # *loop
#     for k in range(i+1):
#         print("*",end="")
#     print()


#6
#sum of N
# n=int(input())
# _sum=0

# while n>0:
#     rem=n%10
#     _sum +=rem
#     n=(n/10)

# print(_sum)



#7

# n=int(input())
# sum=0

# while n>0:
#     rem=n%10
#     _sum=_sum=10+rem
#     n=(n/10)

# # print(_sum)



# #8
# #armstrong
# n=int(input())
# temp=n
# length=0
# temp_size = n 
# _sum=0


# #this part to be find length of n
# while temp_size>0:
#     temp_size=int(temp_size/10)
#     length+=1
# #to find sum
# while n>0:
#     rem=n%10
#     _sum+=(rem**length)
#     n=int(n/10)

# print(temp, _sum, temp_size)
# #to compare
# if temp==_sum:
#     print(f"{temp}is armstrong")
# else:
#     print(f"{temp}is not armstrong")

#9
#armstrong
# _range=int(input())
# for i in range(_range):
#     n=i
#     temp=n
#     length=0
#     temp_size = n 
#     length=0
#     _sum=0


#     #to be find length of n
#     while temp_size>0:
#         temp_size=int(temp_size/10)
#         length+=1
#     #to find sum
#     while n>0:
#         rem=n%10
#         _sum+=(rem**length)
#         n=int(n/10)



#     #to compare
#     if temp==_sum:
#         print(f"{temp}is armstrong")
#     else:
#         print(f"{temp}is not armstrong")


#10
# #functions
# def _sum(a,b):
#     return a+b


# def sub(a,b):
#     return(a-b)


# def mul(a,b):
#     return(a*b)

            
# def div(a,b):
#     return(a/b)


# def modules(a,b):
#     if a>b:
#         return a-b
#     else:
#         return b-a

#     print(_sum(5,6))
#     print(sub(5,6))




#11
#     #Length of n
# def lengthOFN(n):
#     length=0
#     while n>0:
#         len+=1
#         n=int(n/10)
#         return length

# def sumOFN(n,length):
#     _sum=0
#     while n>0:
#         rem=n%10
#         _sum +=(rem ** length)
#         n=int(n/10)
#         return _sum

# def isArmstrong(n,_sum):
#         if n ==_sum:
#             return True
#         else:
#             return False
#             #declaration
# def armstrongInCertainRange(_range):
#         for i in range(_range):
#             n=1
#             length=lengthOFN(n)
#             _sum=sumOFN(n,length)

#         if isArmstrong(n,_sum):
#             print(f"{n} is armstro")
#             #else:
#             #print(f"{n}"is not a)






        















