# for loop + append  사용하기

result = []

for i in range(10):
    result.append(i)
print(result)

# list comprehension 사용하기

result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i%2 == 0]
print(result)

# Nested For loop

word_1 = 'Hello'
word_2 = 'World'
result = [i+j for i in word_1 for j in word_2]

print(result)

# Nested For loop + if문

case_1 = ['A','B','C']
case_2 = ['D','E','A']

result = [i+j for i in case_1 for j in case_2]
print(result)

# if 문 추가

result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)

result.sort()
print(result)

#Split + list comprehension

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for i in stuff:
    print(i)