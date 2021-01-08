# 1

def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x for x in [len(vector) for vector in vector_variables[1:]])

print(vector_size_check([1,2,3],[2,3,4],[5,6,7])) #True
print(vector_size_check([1,3],[2,4],[6,7])) #True
print(vector_size_check([1,3,4],[4],[6,7])) #False

# 2

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [sum(elements) for elements in zip(*vector_variables)]

print(vector_addition([1,3],[2,4],[6,7]))
print(vector_addition([1,5],[10,4],[4,7]))
print(vector_addition([1,3,4],[4],[6,7]))

# 3
