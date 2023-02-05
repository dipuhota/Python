num=int(input('Enter a number (if u want to exit plz enter -)'))
np=0
nn=0
nz=0
while num!=-1:
    if num>0:
       nup=np+1
    elif num<9:
       nn=nn+1
    else:
        nz=nz+1
        num=int(input('Enter a number (if u want to exit plz enter -)'))

print('Number of positive',np)
print('Number of negative',nn)
print('Number of zero',nz)