import math


def func1(a):
    """" 1. Develop a function that returns True if its parameter is even, False otherwise."""
    return a % 2 == 0


def func2(radius):
    """" 2. Develop a function that computes the area of a disc of a given radius."""
    return radius*radius*math.pi


def func3(input_number):
    """" 3. Develop a function that returns the greatest value of a list of positive numbers."""
    input_number.sort(reverse=True)
    return input_number[0]


def func4(input_number):
    """" 4. Develop a function that reverses a list of elements (try to develop an imperative and a recursive
    solution). """
    input_number.reverse()
    return input_number


def func5(number, sortedlist):
    """" 5. Develop a function that inserts a number into an ordered list and returns an ordered list (ascending
    order. This function will be used in the next exercise. """
    sortedlist.append(number)
    sortedlist.sort()
    return sortedlist


def func6(unsorted_list):
    """" 6. Develop a function insertion_sort that takes an unordered list of numbers and returns an ordered list
    taking advantage of the previous function. """
    result = []
    for x in unsorted_list:
        result = func5(x, result)
    return result


def func7_imperative(input_numbers):
    """" 7. Develop an imperative and recursive function that compute the sum of a List of integers without using any
    predefined functions. """
    result = 0
    for x in input_numbers:
        result += x
    return result


def func7_recursive(input_numbers, result, index):
    """" 7. Develop an imperative and recursive function that compute the sum of a List of integers without using any
    predefined functions. """
    if len(input_numbers) == index:
        return result
    return func7_recursive(input_numbers, result + input_numbers[index], index+1)


def lst_len(input_list):
    """8. Develop a function that takes a list of strings and returns a list of integers where the elements are the
    length of the corresponding string. Do not use any predefined functions. Example: lst_len(["abc", "de",
    "fghi"]) returns [3,2,4]
    """
    result = []
    for x in input_list:
        result.append(len(x))
    return result


def flat(input_list):
    """"9. Develop a function that flats a list of lists without using any predefined functions.
        Example: flat([[3,8],[8,9,9],[1,2]]) returns [3,8,8,9,9,1,2]
                 flat([["ab","c"],["d","ef"]]) returns ["ab","c","d","ef"]
                 """
    result = []
    for x in input_list:
        for y in x:
            result.append(y)
    return result


def dic_remove_min_and_max(input_dictionary):
    """"10. Develop a function that takes a dictionary  as parameter and returns another dictionary without both the
    elememts (key, value) that correspond to the maximum and minimum values of the dictionary parameter.
    """
    maximum = max(input_dictionary, key=input_dictionary.get)
    minimum = min(input_dictionary, key=input_dictionary.get)

    del input_dictionary[maximum]
    del input_dictionary[minimum]
    return input_dictionary


def convert_to_binary(input_number):
    """11. Develop a function that takes an integer <= 7 and returns a list of booleans which corresponds to the
    translation into binary of the parameter. Example: 6 = 110 --> [True, True, False].  Tip: try to use a dictionary
     to perform the translation.
    """
    rest = input_number
    result = []
    for i in range(input_number, -1, -1):
        if pow(2, i) <= rest:
            rest -= pow(2, i)
            result.append(True)
        elif len(result) != 0:
            result.append(False)
    return result


def convert_list_to_binary(input_numbers):
    """12. Develop a function that takes a list of integers (each integer <= 7) and returns a list of lists of
    booleans using the previous function.
    """
    result = []
    for x in input_numbers:
        result.append(convert_to_binary(x))
    return result


def merge_lists(input_list):
    """
    Develop a function that transforms a list of lists into another list of lists as follows:
[[x1,x2,x3],[y1,y2,y3], ...] --> [[x1,y1,...],[x2,y2,...],[x3,y3,...]]
The function assumes that all the lists in the input list have the same number of elements.
    """
    result = []
    for i in range(len(input_list[0])):
        result.append([])
        for y in range(len(input_list)):
            result[i].append(input_list[y][i])
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
print("result: "+str(func7_imperative([2, 1, 30, 10, 15]))+" expected: 58")
print("test function7_recursive")
print("result: "+str(func7_recursive([2, 1, 30, 10, 15], 0, 0))+" expected: 58")
print("test lst_len")
print("result: "+str(lst_len(["abc", "de", "fghi"]))+" expected:  [3, 2, 4]")
print("test flat")
print("result: "+str(flat([[3, 8], [8, 9, 9], [1, 2]]))+" expected:  [3, 8, 8, 9, 9, 1, 2]")
print("result: "+str(flat([["ab", "c"], ["d", "ef"]]))+" expected:  [ab, c, d, ef]")
print("test dic_remove_min_and_max")
print("result: "+str(dic_remove_min_and_max({"one": 1, "three": 3, "four": 4, "two": 2}))+" expected: {'three': 3, "
                                                                                          "'two': 2}")
print("test convert_to_binary")
print("result: "+str(convert_to_binary(6))+" expected:  [True, True, False]")
print("result: "+str(convert_to_binary(4))+" expected:  [True, False, False]")
print("test convert_list_to_binary")
print("result: "+str(convert_list_to_binary([5, 6, 2]))+"expected:  [[True, False, True], [True, True, False], [True, "
                                                        "False]]")
print("test merge_lists")
print("result: "+str(merge_lists([[0, 1, 2, 3], [4, 5, 6, 7]]))+" expected:  [[0, 4], [1, 5], [2, 6], [3, 7]]")
print("result: "+str(merge_lists([[0, 1], [4, 5], [2, 3]]))+" expected:  [[0, 4, 2], [1, 5, 3]]")
