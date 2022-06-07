def fibonacciSequence():
    n1, n2, i = 1, 2, 0
    sum = 0
    while n1 < 4000000:
    
        if n1 % 2 == 0:
            sum += n1
        nth = n1 + n2
        n1 = n2
        n2 = nth
        i += 1
    print("sum : ",sum)

fibonacciSequence()