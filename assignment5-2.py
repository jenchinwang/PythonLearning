## This program will allow user to enter a series of number until user hit done.
## In the end the program is going to return the smallest largest number user has entered.
largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : 
        break
    try:
        num = int(inp)
    except:
        print "Invalid input"
        continue
    if (largest and smallest) is None:
        largest = num
        smallest = num  
    if num < smallest:
            smallest = num
    if num > largest:
            largest = num
    print largest, smallest, num
print "Maximum is", largest
print "Minimum is", smallest