import math

def specialPythagoreanTriplet ():
    number = []
    for a in range(1, 2000):
        for b in range(1, 2000):
            for c in range(1, 2000):
                if a < b and b < c:
                    print(a, b, c)
                    # if ((math.sqrt(a) + math.sqrt(b)) == math.sqrt(c) and (a + b + c) == 1000):
                    if ((math.sqrt(a) + math.sqrt(b)) == math.sqrt(c)):
                        # print((a + b + c))
                        d = (a + b + c)
                        number.append(d)
    return number

print(specialPythagoreanTriplet())