import math


def func1(a):
    """" 1. Develop a function that returns True if its parameter is even, False otherwise."""
    return a % 2 == 0


def func2(radius):
    """" 2. Develop a function that computes the area of a disc of a given radius."""
    return radius*radius*math.pi


def func3(input):
    """" 3. Develop a function that returns the greatest value of a list of positive numbers."""
    input.sort(reverse=True)
    return input[0]


def func4(input):
    """" 4. Develop a function that reverses a list of elements (try to develop an imperative and a recursive
    solution). """
    input.reverse()
    return input


def func5(number, sortedlist):
    """" 5. Develop a function that inserts a number into an ordered list and returns an ordered list (ascending
    order. This function will be used in the next exercise. """
    sortedlist.append(number)
    sortedlist.sort()
    return sortedlist


def func6(unsortedlist):
    """" 6. Develop a function insertion_sort that takes an unordered list of numbers and returns an ordered list
    taking advantage of the previous function. """
    result = []
    for x in unsortedlist:
        result = func5(x, result)
    return result


def func7_imperativ(input):
    """" 7. Develop an imperative and recursive function that compute the sum of a List of integers without using any
    predefined functions. """
    result = 0
    for x in input:
        result += x
    return result


print("test function1")
print("result: "+str(func1(1))+" expected: False")
print("result: "+str(func1(2))+" expected: True")
print("test function2")
print("result: "+str(func2(20))+" expected: 1256.63706")
print("test function3")
print("result: "+str(func3([1, 2, 3, 10]))+" expected: 10")
print("test function4")
print("result: "+str(func4([1, 2, 3, 10]))+" expected: [10, 3, 2, 1]")
print("test function5")
print("result: "+str(func5(6, [1, 2, 3, 10, 15]))+" expected: [1, 2, 3, 6, 10, 15]")
print("test function6")
print("result: "+str(func6([2, 1, 30, 10, 15]))+" expected: [1, 2, 10, 15, 30]")
print("test function7_imperative")
print("result: "+str(func7_imperativ([2, 1, 30, 10, 15]))+" expected: 58")
