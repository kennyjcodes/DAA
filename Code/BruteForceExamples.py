# number = int(input("Enter value to search: "))

from array import array


def searchVal(number, array):
    for i in range(0, len(array) - 1):
        if (array[i] == number):
            return 1
    return 0


print(searchVal(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def countOccurence(array, number):
    count = 0
    for i in range(0, len(array) - 1):
        if (array[i] == number):
            count += 1
    return count


print(countOccurence([1, 1, 1, 2, 3, 4, 5, 6, 1, 7, 8, 4], 1))


def squareNumber(array, square, x4):
    for i in range(len(array)):
        square[i] = array[i] * array[i]

    for j in range(len(array)):
        x4[j] = array[j] * array[j] * array[j] * array[j]

    return square, x4


def main():
    array = [1, 2, 3, 4, 5]
    sq = [0] * len(array)
    x4 = [0] * len(array)
    print(squareNumber(array, sq, x4))


main()


def diagonalMatrixSum(matrix):
    # Bruteforce:
    sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if (row == col):
                sum += matrix[row][col]
    return sum


def diagonalMatrix(matrix):
    # optimal:
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(diagonalMatrix(matrix))


main()


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if (array[i] < array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


def main():
    array = [2, 7, 4, 1, 9, 5, 11, 3]
    print(bubbleSort(array))


main()
