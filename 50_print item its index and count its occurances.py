# Wap to Search an avlue from a list then display it index
# if the value is present multiple times then prints its all indices and
# also count the number of times that value is repeated in the

from itertools import count


l = [10, 20, 30, 40, 10, 20, 10, 20, 10, 30, 50]
i = 0
count= 0
key = int(input('enter the key to search:'))
while i < len(l):
    if key == l[i]:
        print(f'{key} is present at {i} index')
        count=count+1
    i = i + 1
print(f'{key} is pre4sent {count} times')

