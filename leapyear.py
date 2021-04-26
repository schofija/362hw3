year = input("Input a year: ")

fourRem = int(year) % 4
oneHundredRem = int(year) % 100
fourHundredRem = int(year) % 400

if fourRem != 0:
    print("Not a leap year")
    quit()
    
else:
    if oneHundredRem == 0:
        if fourHundredRem != 0:
            print("Not a leap year")
            quit()
        else:
            print("Leap year!")
            quit()
    else:
        print("Leap year!")
        quit()