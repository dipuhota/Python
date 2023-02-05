# myinfo={
#     'name':'dipu hota',
#     'email':'dipuhota7@gmail.com',
#     'address':'kendrapada',
#     'mobile':8117904544,
# }


# print(myinfo['name'])
# print(myinfo)


#Duplicate key are not allowed
# myinfo={
#     'name':'dipu hota',
#     'Name':'poonam',
#     'email':'dipuhota7@gmail.com',
#     'address':'kendrapada',
#     'mobile':8117904544,
# }
# print(myinfo['name])



#Diffrent ways for creating dict
# empy dict
# d={}
# print(d)
# print(type(d))



#create empty dict then add item
# d={}
# d['name']='dipu'
# d['address']='kendrapada'
# d['email']='dipuhpta7@gmail.com'

# print(d)



#create dict directly
# roll={1:'dipu',2:'poonam',3:'rahul',4:'sourav'}
# print(roll)


# roll={1:'dipu',2:'poonam',3:'rahul',4:'sourav'}
# print(roll[11])            #keyError




# roll={1:'dipu',2:'poonam',3:'rahul',4:'sourav'}
# print(roll[0])     

# check the key is exists or not
#has_key()

# roll={1:'dipu',2:'poonam',3:'rahul',4:'sourav'}
# print(roll.has_key(2))     


# solution 
#use in operater

# roll={1:'dipu',2:'poonam',3:'rahul',4:'sourav'}
# print(2 in roll)     
# print(2 not in roll)     


#create a dictionary dynamicically by tacking user input
# d={}

# while True:
#     key=input('Enter the key : ')
#     val=input('Enter the value : ')
#     d[key]=val
    
#     choice=input('Do you want to add more element [Y/N')
#     if choice== 'N':
#         break
#     print(d)


# Traversing a dict
# roll={1:'dipu', 2:'poonam', 3:'rahul', 4:'sourav'}

#print only keys
# for i in roll:
#     print(i)

 

#print key and value

# roll={1:'dipu', 2:'poonam', 3:'rahul', 4:'sourav'}

# for i in roll:
#     print(i,roll[i])


#additem in a dictionry

# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)
# d[27]='anjali'
# print(d)

#modify

# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)
# d[24]='anjali'
# print(d)
# d[1024]='hello'
# print(d)


#delete item
# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)
# del d[26]
# print(d)

# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)
# del d[123]
# print(d)



#delete all the item
# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)
# d.clear()
# print(d)



# how to delete entire dict

# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)
# del d
# print(d)

#dict key immutable in nature hence we cant use list , 
# set ,dict as a dict key but we can use Number,Tuple,
# Frozenset as a dict key otherwise we will get TypeError.

# d={[21,22,2323]:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)

# d={(21,22,2323):'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)

# l=[21,22,23]
# d={l:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)

# l.append(100)


# s=set ((10,20,30))
# d={s:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)



# s=set ((10,20,30))
# d={frozenset(s):'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)

# s=set ((10,20,30))
# d={frozenset(s):'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d[frozenset({10, 20, 30})])




# d={12.3:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)

# d={12+13j:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)

# d={True:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)




# d={{1:'one'}:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# print(d)


# d={23:'dipu',24:'poonam',25:'rahul',26:'sourav'}
# # print(d)
























