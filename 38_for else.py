# for else
# for loop excecute fully without having any break

# for i in range(10):
#     print(i)
# else:
#     print("i am else block")    


#if break exicuted inside for loop then our else block
#wont be exicute
for i in range(10):
    if i==6:
        break
    print(i)
else:
    print("i am else block")
