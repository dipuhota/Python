
# l=[10,20,30,40,50]
# s=['chandan','dipu',999,888,777]
# r=l+s
# print(r)




# l=[10,20,30,40,50]
# s=['chandan','dipu',999,888,777]
# a=[12.3,45.67,True,False]
# r=l+s
# print(r)


# l=[10,20,30,40,50]
# r=[l*5]
# print(r)


# l=[10,20,30,40,50]
# r=[l*5.7]
# print(r)


# l=[10,20,30,40,50]
# r=[l*l]
# print(r)


#membership operater (in,not in)

# l=[10,20,30,40,50]
# print(20 in l)
# print(20 not in l)
# print(999 in l)
# print(999 not in l)


# wap to check wheather your lucky number is present inside list or not

# l=[1,2,4,6,7,8,11,12,17,18,23,55,73,87,92,99]
# choice=int(input("Enter your lucky number :"))

# if choice in l:
#     print("yes your lucky number is available")

# else:
#     print("sorry lucky number is not available")

from xml.etree.ElementPath import prepare_descendant


l=[1,2,4,6,7,8,11,12,17,18,23,55,73,87,92,99]

choice=int(input("Enter your lucky number : "))

while True:
    if choice in l:
        print("yes u r lucky number is present")
    else:
        print("sry u r lucku is not prepare")
        choice=int(input("Enter your lucky number again:"))














