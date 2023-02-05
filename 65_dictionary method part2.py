#list method part
#keys()
# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d.keys())



# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# for i in d.keys():
#     print(i)

#values()
# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d.values())

# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# for i in d.values():
#     print(i)

#setdefault()
# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)
# print(d.setdefault(23,'anjali'))
# print(d)

# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)
# print(d.setdefault(999,'anjali'))
# print(d)

#update()
# d1={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# d2={1:'college',2:'university'}
# d1.update(d2)

# print(d1)
# print(d2)

# d1={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# d2={23:'college',2:'university'}
# d1.update(d2)

# print(d1)
# print(d2)



#copy()

# d1={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# d2={}
# d2=d1.copy()
# # print(d1)
# # print(d2)

# print(id(d1))
# print(id(d2))

# d1[24]='anjali'

# print(d1)
# print(d2)

# d1={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# d2={}
# d2=d1
# # print(d1)
# # print(d2)

# print(id(d1))
# print(id(d2))

# d1[24]='anjali'

# print(d1)
# print(d2)


#clear()
# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# d.cler()
# print(d)


#formkeys()
# l=(23,33,43,53,63)
# d=dict.formkeys(l)
# print(d)

# l=[23,33,43,53,63]
# d=dict.formkeys(l,'hello')
# print(d)


# d=dict.formkeys(range(5),[1,2,3])
# print(d)


# d=dict.formkeys([1],[1])
# print(d)

l=[23,33,43,53,63]
d={}.fromkeys(l)
print(d)
