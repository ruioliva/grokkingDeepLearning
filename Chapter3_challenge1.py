def elementwise_multiplication(vec_a, vec_b):
    assert (len(vec_a) == len(vec_b))

    total = 1
    for index in range(len(vec_a)):
        total *= vec_a[index] * vec_b[index]

    return total


def elementwise_addition(vec_a, vec_b):
    assert (len(vec_a) == len(vec_b))

    total = 0
    for index in range(len(vec_a)):
        total += vec_a[index] * vec_b[index]

    return total


def vector_sum(vec_a):
    total = 0
    for index in range(len(vec_a)):
        total += vec_a[index]

    return total


def vector_average(vec_a):
    total = 0
    for index in range(len(vec_a)):
        total += vec_a[index]

    return total / len(vec_a)


vector_a = [6, 3, 4.5, 9.8, 1.4]
vector_b = [-2, 4, 8.5, 2.8, 3.4]

print(vector_a)
print(vector_b)
print(elementwise_multiplication(vector_a, vector_b))
print(elementwise_addition(vector_a, vector_b))
print(vector_sum(vector_a))
print(vector_average(vector_a))
