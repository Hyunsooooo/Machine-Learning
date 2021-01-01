# Enumerate

## list의 element를 추출할 때, 번호를 붙여서 추출
print(dict(enumerate(['tic','tac','toe'])))

for i,v in enumerate(['a','b','c']):
    print(i,v)

# list에 있는 index와 값을 unpacking하여 list로 저장

mylist = ['a','b','c','d']
print(list(enumerate(mylist)))


# 문장을 list로 만들고 list의 index와 값을 unpacking하여 dict로 저장

print({i:j for i,j in enumerate('Gachon University is an academic institute located in South Korea.'.split())})

#Zip

# for loop + zip

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for a,b in zip(alist,blist):
    print(a,b)

# list comprehension + zip

a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)

print([sum(x) for x in (a,b,c)])
print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])

# enumerate + zip

for i,(a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)