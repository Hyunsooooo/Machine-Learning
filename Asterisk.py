# Asterisk
## *args 한꺼번에 받아서 처리 (튜플), **kargs(dict)
def asterisk_test(a,*args):
    print(a,args)
    print(type(args))

print(asterisk_test(1,2,3,4,5,6))

def asterisk_test2(a,**kargs):
    print(a,kargs)
    print(type(kargs))

print(asterisk_test2(1, b=1, c=3, d=4, e=5, f=6))


# Asterisk - unpacking a container
## *로 unpacking을 할 수 있음
def asterisk_test(a,*args):
    print(a,args)
    print(type(args))

print(asterisk_test(1,(2,3,4,5,6)))

def asterisk_test(a,args):
    print(a,*args)
    print(type(args))

print(asterisk_test(1,(2,3,4,5,6)))

#

a,b,c = ([1,2],[3,4],[5,6])
print(a,b,c)

data = ([1,2],[3,4],[5,6])
print(data)
print(*data)

def asterisk_test(a,b,c,d):
    print(a,b,c,d)

data = {'b':1, 'c':2, 'd':3}
print(asterisk_test(10,**data))
# print(asterisk_test(10,data)) error

for data in zip(*([1,2],[3,4],[5,6])):
    print(data)
# *로 unpacking을 해서 zip으로 병렬 나열.


def asterisk_test(a,b,c,d,e=0):
    print(a,b,c,d,e)
data = {'d':1, 'c':2, 'b':3, 'e':56}
print(asterisk_test(10,**data))
