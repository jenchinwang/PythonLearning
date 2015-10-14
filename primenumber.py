def is_prime(x):
    # only positive numbers are allowed and the smallest prime number is 2 
    if (x > 1):
        # since the smallest prime number is 2, we start the divisor at 3
        divisor = 2

        # because the submit number can always be divided by itself we can use the
        # range function to set the correct range
        for i in range(divisor,x):
            if (x % i) == 0:
                print "%d is not a prime number." % x
                return False
    else:
        print "%d is not a prime number." % x
        return False
    print "%d is a prime number." % x
    return True

inp = raw_input('Please enter a number: ')
inp = int(inp)
print is_prime(inp)