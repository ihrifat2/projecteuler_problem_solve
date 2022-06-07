def getSum():

    number = 1000
    sum = 0

    for num in range(1, number):
        if num != 0:
            if num % 3 == 0 or num % 5 == 0:
                sum += num
                # print(num)
    return sum

print(getSum())