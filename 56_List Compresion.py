# l=[i for i in range(11)]
# print(l)

# l=[i*i for i in range(11)]
# print(l)

# l=[i**i for i in range(11)]
# print(l)

# l=[i+10 for i in range(11)]
# print(l)

#With using LC
# l=[i for i in range(1,21) if i % 2 == 0]
# print(l)


#Without using LC
# l = []
# for i in range(1, 21):
#     if i%2==0:
#         l.append(i)
# print(l)


# name=['dipu','poonam','tapan','rahul']
# excepted output : ['d','p','t','r']


# names=['dipu','poonam','tapan','rahul']
# l=[i[0] for i in names]
# print(l)



# names=['dipu','poonam','tapan','rahul']
# l=[i[0:4] for i in names]
# print(l)

#create a new list by add  the element which 
#is containg letter a
# names=['dipu','poonam','tapan','rahul']

# l=[i for i in names if 'a' in i]
# print(l)


#
# names=['dipu','poonam','tapan','rahul']

# l=[i if i!='poonam' else 'hello' for i in names]
# print(l)

#create a list from tuple
# t=(10,20,30,40,50)
# l=[i for i in t if i % 6 ==0]
# print(l)

#create a list from string
# name="dipu"
# l=[i for i in name]
# print(l)


#creation of matrix using list com..
# m=[[i for j in range(5)] for i in range(5)]
# print(m)


# m=[[i*j for j in range(5)] for i in range(5)]
# print(m)


