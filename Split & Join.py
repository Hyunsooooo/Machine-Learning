# 일반 코드

colors= ['a','b','c','d','e']
result  = ''

for s in colors:
    result += s
print(result)

# pythonic code

colors= ['red','blue','green','yellow']
result = ''.join(colors)

print(result)

# Split 함수

items = 'zero one two three'.split()
print(items)

example = 'python,jquery,javascript'
print(example.split(','))

a,b,c, = example.split(',')
#example을 split한 걸 a,b,c 변수로 unpacking

example = 'cs50.gachon.edu'

subomain, domain, tld = example.split('.')
print( subomain, domain, tld)

# Join함수

## string list를 합쳐 하나의 string으로 반환할 때 사용

colors= ['red','blue','green','yellow']
result = ''.join(colors)
print(result)

result = ' '.join(colors)
print(result)

result = ', '.join(colors)
print(result)

result = '-'.join(colors)
print(result)