# 컴퓨터는 문자를 그대로 이해하지 못한다. 컴퓨터로 처리하기 위해서 문자 -> 숫자로 표현해야함
# 숫자로 유사하다는 어떻게 표현하는가? 유사하다 = 가깝다 로 해석하여 좌표가 가깝다. 로 해석

# 문자를 Vector로 - One-hot Encoding
# - 하나의 단어를 Vector 의 Index 로 인식, 단어 존재시 1 없으면 0

# Bag of words
# - 단어별로 인덱스를 부여해서, 한 문장(또는 문서)의 단어의 개수를 Vector 로 표현.

# Euclidian Distance
# - 피타고라스 정리, 점과 점 사이의 거리 공식

# Cosine Distance
# - 두 점 사이의 각도, 벡터의 내적
# 영상 8:08

# Euclidian Distance 보다 Cosine Distance를 많이 활용한다.
# - [4,0] 에서 [4,1] 과 [5,0] 의 거리 차이를 Euclidian은 정확히 표현하지 못한다.

# 야구선수의 영문 기사를 분류하기

#  Process
# - 파일을 불러오기
# - 파일을 읽어서 단어사전 (corpus) 만들기
# - 단어별로 index 만들기
# - 만들어진 index로 문서별로 Bag of words vector 생성
# - 비교하고자 하는 문서 비교하기
# - 얼마나 맞는지 측정하기

import os

# 파일 불러오기
def get_file_list(dir_name):
    return os.listdir(dir_name)

if __name__ == "__main":  # __name__ 이 무엇을 의미하는 건지
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name,file_name) for file_name in file_list]

# 파일별로 내용 읽기
def get_contents(file_list):
    y_class = []
    x_text = []
    class_dict = {
        1: '0', 2: '0', 3: '0', 4: '0', 5:'1', 6:'1', 7:'1', 8:'1'}

    for file_name in file_list:
        try:
            f = open(file_name, 'r' , encoding = 'cp949')
            category = int(file_name.split(os.sep)[1].split('_')[0])
            y_class.append(class_dict[category])
            x_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return x_text,y_class

# Corpus 만들기 + 단어별 index 생성하기

def get_cleaned_text(text): # 의미없는 문장 보호 제거하기
    import re
    text = re.sub('\+','',text.lower())
    return text

def get_corpus_dict(text):
    text= [sentence.split() for sentence in text] # text에서 sentence를 받아서 split 해준 걸 다시 text에 할당 text에는 단어 개수대로 잘라진 2dim-list
    cleaned_words = [get_cleaned_text(word)for words in text for word in words] # text에서 word를 다시 1글자씩 뽑아서 1dim array로 반환

    from collections import OrderedDict
    corpus_dict = OrderedDict()
    for i, v in enumerate(set(cleaned_words)):
        corpus_dict[v] = i
    return corpus_dict


# 문서별로 Bag of words vector 생성

def get_count_vector(text,corpus):
    text = [sentence.split() for sentence in text]
    word_number_list = [[corpus[get_cleaned_text(word)]for word in words] for words in text]
    x_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))]

    for i, text in enumerate(word_number_list):
        for word_number in text:
            x_vector[i][word_number] +=1
    return x_vector


# 비교하기

import math
def get_cosine_similarity(v1,v2):
    'compute cosine similarity of v1 to v2 : (v1 dot v2)/{||v1||*||v2||)'
    sumxx, sumxy, sumyy = 0,0,0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)


# 비교결과 정리하기

def get_similarity_score(x_vector, source):
    source_vector = x_vector[source]
    similarity_list = []
    for target_vector in x_vector:
        similarity_list.append(get_cosine_similarity(source_vector,target_vector))
        return similarity_list

def get_top_n_similarity_news(similarity_score, n):
    import operator
    x = {i:v for i,v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key = operator.itemgetter(1))

    return list(reversed(sorted_x))[1:n+1]


from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
corpus = [\
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?']
X = vectorizer.fit(corpus)
print(X.__dict__)