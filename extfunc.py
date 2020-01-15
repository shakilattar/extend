def extfunc():
    num1 = [4, 9, 16]
    num2 = [25, 36, 49]
    print(num1)
    print(num2)
    # add all the values of num2 into num1
    num1.extend(num2)
    
    print(num1)
    print(num2)


extfunc()
