
def getFactor(myList,number):
    # myList : expected list or tuple
    # number : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    factors = []

    x= [i for i in myList if number % i == 0] #make i not use 0
    factors.extend(x)

    print(factors)
    return factors

if getFactor(range(10),12) == [1,2,3,4,6]:
    print("yay")
else:
    print("nay")