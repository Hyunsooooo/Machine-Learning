# lambda의 정의

def f(x,y):
    return x+y

print(f(1,4))

f = lambda x,y : x+y
print(f(1,4))

# Map function
## Sequence 자료형 각 element에 동일한 function을 적용함

ex = [1,2,3,4,5]
f = lambda x,y: x+y
print(list(map(f,ex,ex)))

a = list(map(\
    lambda x: x**2 if x%2 ==0 else x, ex))

print(a)


# Reduce function
## map function과 달리 list에 똑같은 함수를 적용해서 통합

from functools import reduce

print(reduce(lambda x,y:x+y,[1,2,3,4,5]))
# 1+2 =3, 3+3= 6, 6+4 = 10, 10+5 = 15
# index=0부터 처리해 나감

def factorial(a):
    return reduce(lambda x,y:x*y, range(1,a+1))

print(factorial(5))