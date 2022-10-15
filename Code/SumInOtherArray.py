# Design an ALGORITHM which takes 10 consecutive numbers in a linear structure(e.g. 1 Dimensional array) and add like this to put the sum in another array.
# For example, if the array is {1,2,3,4,5,6,7,8,9,10}, the result array should be {1,3,6,10,15,21,28,36,45,55}

def sumArray(array, res):
    for i in range(0, len(array)):
        sum = 0
        for j in range(i+1):
            sum += array[j]
        res[i] = sum
    return res


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = [0]*len(array)
    res = sumArray(array, res)
    print(res)


if __name__ == "__main__":
    main()


# def sumArray(array, res):
#     res[0] = array[0]
#     for i in range(1, len(array)):
#         res[i] = res[i-1] + array[i]
#     return res


# Design an ALGORITHM which takes 10 consecutive numbers in a linear structure(e.g. 1 Dimensional array) and take their factorial in another array.
# For example, if the array is {1,2,3,4,5,6,7,8,9,10}, the result array should be {1,2,6,24,120,720,5040,40320,362880,3628800}

def factorialArray(array, res):
    for i in range(0, len(array)):
        factorial = 1
        for j in range(i+1):
            factorial *= array[j]
        res[i] = factorial
    return res


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = [0]*len(array)
    res = factorialArray(array, res)
    print(res)


if __name__ == "__main__":
    main()
