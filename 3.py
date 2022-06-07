import math

def sumOfHundradAndSquare():
    i = 1
    sumSquareNutualNumber = 0
    squareSumNutualNumber = 0
    while i <= 100:
        sumSquareNutualNumber += i**2
        squareSumNutualNumber += i
        print(i)
        i += 1
    print("sumSquareNutualNumber : ", sumSquareNutualNumber)
    squareSumNutualNumber = squareSumNutualNumber**2
    print("squareSumNutualNumber : ", squareSumNutualNumber)
    difference = squareSumNutualNumber - sumSquareNutualNumber
    print("difference : ", difference)
sumOfHundradAndSquare()